def remove_repeat_chars(s: str) -> str:
    start_index, end_index = (7, 9)
    chars_to_remove = []
    for i in range(start_index, end_index):
        if s[i] not in chars_to_remove:
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        if s.count(char) > 1:
            s = s.replace(char, '', s.count(char) - 1)
    return ''.join((char if i < start_index or i >= end_index else '' for i, char in enumerate(s)))