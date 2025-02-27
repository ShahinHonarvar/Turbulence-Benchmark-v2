def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(len(char_list)):
        if 61 <= i <= 70 and '0' <= char_list[i] <= '@':
            char_list[i] = ''
    return ''.join(char_list)