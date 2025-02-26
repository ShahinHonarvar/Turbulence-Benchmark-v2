from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:10].lower()
    letter_counts = {}
    for char in letters:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_counts = {}
            for char in perm:
                if char.isalpha():
                    perm_counts[char] = perm_counts.get(char, 0) + 1
            if all((perm_counts.get(char, 0) <= letter_counts.get(char, 0) for char in perm_counts)):
                sorted_perm = sorted(perm)
                for i in range(length - length // 2):
                    if sorted_perm[i] != sorted_perm[length - i - 1]:
                        break
                else:
                    palindrome = ''.join(perm)
                    palindrome_set.add(palindrome)
    return palindrome_set