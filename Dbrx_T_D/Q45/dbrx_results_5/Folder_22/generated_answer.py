from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def extend_palindrome(i, j):
        while i > 0 and j < len(s) and (s[i - 1].lower() == s[j].lower()):
            i -= 1
            j += 1
        return s[i:j + 1]
    palindromes = set()
    english_letters = defaultdict(list)
    for i, c in enumerate(s):
        if c.isalpha():
            english_letters[c.lower()].append(i)
    for start in english_letters['e']:
        for end in english_letters['t']:
            if start > end:
                continue
            palindrome = extend_palindrome(start, end)
            if is_palindrome(palindrome) and len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes