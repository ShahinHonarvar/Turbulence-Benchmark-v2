def filter_chars(s):
    chars_to_remove = [c for c in s[20:63] if c >= 'i' and c <= 'k']
    result = ''
    for c in s:
        if c not in chars_to_remove:
            result += c
    return result