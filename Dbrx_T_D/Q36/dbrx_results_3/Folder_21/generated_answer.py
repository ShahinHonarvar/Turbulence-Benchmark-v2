def filter_chars(s: str) -> str:
    start_index = 218
    end_index = 403
    min_char = '*'
    max_char = '7'
    for i in range(start_index, end_index):
        char = s[i]
        if char > min_char and char < max_char:
            s = s.replace(char, '', 1)
    return s