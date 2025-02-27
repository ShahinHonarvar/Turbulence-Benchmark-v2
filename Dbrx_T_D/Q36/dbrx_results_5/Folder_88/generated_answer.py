def filter_chars(s: str) -> str:
    start_index, end_index = (78, 81)
    for i in range(start_index, end_index):
        char_to_filter = s[i]
        if 'S' < char_to_filter < '[':
            s = s.replace(char_to_filter, '', 1)
    return s