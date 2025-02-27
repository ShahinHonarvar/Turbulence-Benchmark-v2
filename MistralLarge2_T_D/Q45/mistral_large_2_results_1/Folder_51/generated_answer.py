from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:6].lower()
    letters = set(filter(str.isalpha, substring))
    all_palindromes = set()
    for length in range(3, len(substring) + 1):
        for p in permutations(letters, length):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                all_palindromes.add(palindrome)
    return all_palindromes