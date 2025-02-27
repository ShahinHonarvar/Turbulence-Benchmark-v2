def filter_chars(s):
    chars_to_remove = [c for c in s[38:55] if ':' <= c <= 'r']
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result