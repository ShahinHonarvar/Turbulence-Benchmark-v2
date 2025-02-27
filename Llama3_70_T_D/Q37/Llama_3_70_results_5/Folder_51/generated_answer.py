def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s[:41]) if 36 <= i <= 40 and 'H' <= char <= 'e']
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result