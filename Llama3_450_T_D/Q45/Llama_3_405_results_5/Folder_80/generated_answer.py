import itertools

def palindromes_between_indices(s):
    substr = ''.join(filter(str.isalpha, s[3:9])).lower()
    unique_chars = ''.join(set(substr))
    palindromes = set()
    for r in range(7, len(substr) + 1):
        for perm in itertools.permutations(unique_chars, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes