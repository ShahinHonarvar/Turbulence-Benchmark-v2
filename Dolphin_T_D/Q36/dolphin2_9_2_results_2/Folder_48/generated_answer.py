def filter_chars(s):
    index_start = 154
    index_end = 222
    chars_to_remove = [s[i] for i in range(index_start, index_end) if 'A' < s[i] < 'f']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s