from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:8] if char.isalpha()]
    palindrome_set = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            for i in range(len(perm) - length + 1):
                subset = perm[i:i + length]
                if len(subset) >= 7 and list(subset) == list(subset)[::-1]:
                    palindrome = ''.join(subset)
                    palindrome_set.add(palindrome)
    return palindrome_set