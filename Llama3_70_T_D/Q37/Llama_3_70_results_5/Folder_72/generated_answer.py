def filter_chars(s):
    result = ''
    chars_to_remove = set()
    for i in range(35, 52):
        if i < len(s) and 'H' <= s[i] <= 's':
            chars_to_remove.add(s[i])
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result