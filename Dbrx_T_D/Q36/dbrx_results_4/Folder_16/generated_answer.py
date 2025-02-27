def filter_chars(s):
    start_index = 331
    end_index = 713
    chars_to_remove = []
    for i in range(start_index, end_index):
        if 'M' < s[i] < '_':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s