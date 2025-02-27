from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join((c for c in s if c.isalpha()))
    substring = s[1:9]
    palindromes = set()
    for perm in permutations(substring, len(substring)):
        word = ''.join(perm)
        for length in range(7, len(word) + 1):
            for i in range(len(word) - length + 1):
                if is_palindrome(word[i:i + length]):
                    palindromes.add(word[i:i + length])
    return palindromes