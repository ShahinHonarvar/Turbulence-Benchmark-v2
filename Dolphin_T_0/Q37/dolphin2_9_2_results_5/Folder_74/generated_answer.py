def filter_chars(s):
    chars_to_remove = [s[i] for i in range(19, 33) if 'f' <= s[i] <= 'o']
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result