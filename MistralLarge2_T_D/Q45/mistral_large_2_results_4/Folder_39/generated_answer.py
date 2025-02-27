from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6]
    english_letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes