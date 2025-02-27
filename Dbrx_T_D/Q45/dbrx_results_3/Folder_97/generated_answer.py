from collections import defaultdict
    import string

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    english_letters = {c for c in string.ascii_letters}
    for i in range(5):
        for j in range(i, 5):
            substring = s[i:j + 1]
            candidates = [''.join(p) for p in itertools.product(english_letters, repeat=len(substring)) if len(p) >= 3]
            for candidate in candidates:
                if is_palindrome(candidate) and candidate.lower() in substring.lower():
                    palindromes.add(candidate)
    return palindromes