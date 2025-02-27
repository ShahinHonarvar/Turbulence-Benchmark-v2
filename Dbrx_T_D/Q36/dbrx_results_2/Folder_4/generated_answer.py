def filter_chars(s: str) -> str:
    start_index, end_index = (42, 67)
    chars_to_remove = []
    for i in range(start_index, end_index):
        if '6' < s[i] < 'g':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s