def filter_chars(s: str) -> str:
    start_index = 21
    end_index = 25
    for i in range(start_index, end_index):
        char = s[i]
        if '5' < char < '}':
            s = s.replace(char, '', 1)
    return s