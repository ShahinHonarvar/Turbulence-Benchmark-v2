def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(len(char_list)):
        if 38 <= i <= 99 and 'A' <= char_list[i] <= 'Q':
            char_list[i] = ''
    return ''.join(char_list)