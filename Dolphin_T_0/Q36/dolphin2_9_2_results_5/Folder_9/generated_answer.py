def filter_chars(s):
    chars_to_remove = [s[i] for i in range(50, 92) if s[i] > 'A' and s[i] < 'Q']
    new_s = ''
    for char in s:
        if char not in chars_to_remove:
            new_s += char
    return new_s