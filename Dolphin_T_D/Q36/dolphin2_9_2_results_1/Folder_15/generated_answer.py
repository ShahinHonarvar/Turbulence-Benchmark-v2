def filter_chars(s):
    chars_to_remove = [s[i] for i in range(2, 7) if 'h' < s[i] < 'k']
    new_s = []
    for char in s:
        if char not in chars_to_remove:
            new_s.append(char)
    return ''.join(new_s)