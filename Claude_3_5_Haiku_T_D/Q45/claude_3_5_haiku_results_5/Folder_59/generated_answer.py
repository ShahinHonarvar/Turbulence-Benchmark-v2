from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    letters_in_range = s[8:10].lower()
    english_letters = [char for char in letters_in_range if char.isalpha()]
    if len(english_letters) < 3:
        return set()
    palindrome_set = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            for i in range(len(perm)):
                candidate = list(perm)
                mid = len(candidate) // 2
                left = candidate[:mid]
                right = candidate[mid + len(candidate) % 2:]
                right.reverse()
                if left == right:
                    palindrome = ''.join(candidate)
                    palindrome_set.add(palindrome)
    return palindrome_set