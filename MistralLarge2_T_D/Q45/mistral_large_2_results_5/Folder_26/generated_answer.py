from itertools import permutations

def palindromes_between_indices(string):
    substring = ''.join(filter(str.isalpha, string[4:7])).lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes