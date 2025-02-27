def filter_chars(s):
    chars_to_remove = [c for c in s[36:79] if ord('a') <= ord(c) <= ord('i')]
    result = ''
    for c in s:
        if c not in chars_to_remove:
            result += c
    return result