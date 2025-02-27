def filter_chars(s):
    chars_to_remove = [c for c in s[36:80] if c >= 'a' and c <= 'i']
    result = ''.join([c for c in s if c not in chars_to_remove])
    return result