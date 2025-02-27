import string

def palindromes_between_indices(s):
    english_letters = set(string.ascii_letters) & set(s.lower())
    return set((''.join(palindrome) for length in range(7, 1 + s.count(s[0], 0, 7)) for palindrome in itertools.combinations_with_replacement(english_letters, length) if is_palindrome(''.join(palindrome))))

def is_palindrome(s):
    return s == s[::-1]