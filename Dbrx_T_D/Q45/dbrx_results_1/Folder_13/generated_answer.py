from fro027_sup import group_chars_by_type, is_palindrome

def palindromes_between_indices(s):
    allowed_chars = group_chars_by_type(s[3:10], 'alphanumeric', case_sensitive=False)
    palindromes = {w for w in itertools.product(allowed_chars, repeat=5) if is_palindrome(''.join(w))}
    return palindromes