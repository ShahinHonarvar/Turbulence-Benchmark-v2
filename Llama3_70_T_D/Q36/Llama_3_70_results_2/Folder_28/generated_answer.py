def filter_chars(s):
    s = list(s)
    chars_to_remove = set()
    for i in range(31, 73):
        if s[i] > 'M' and s[i] < 'j':
            chars_to_remove.add(s[i])
    s = [char for char in s if char not in chars_to_remove]
    return ''.join(s)