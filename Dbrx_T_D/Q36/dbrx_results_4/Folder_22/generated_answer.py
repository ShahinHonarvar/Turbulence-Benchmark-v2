def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(len(char_list)):
        if 55 < i < 84:
            if char_list[i] > ';' and char_list[i] < 'z':
                char_list = [char for char in char_list if char != char_list[i]]
    return ''.join(char_list)