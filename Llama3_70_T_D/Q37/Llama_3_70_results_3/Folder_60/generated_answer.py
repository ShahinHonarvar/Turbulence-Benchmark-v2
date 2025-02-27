def filter_chars(s):
    chars_to_remove = set(s[12:78])
    chars_to_remove = {c for c in chars_to_remove if ord(':') <= ord(c) <= ord('L')}
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result