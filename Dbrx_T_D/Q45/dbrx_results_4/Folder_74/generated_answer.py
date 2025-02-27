import re
    from string import ascii_lowercase

def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]
    letters = ''.join(set(re.findall('[a-z]', s.lower())))
    palindromes = {p for l in letters for p in permutations(l, 6) if is_palindrome(p)}
    return palindromes