def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(4, 8):
        if '1' < char_list[i] < 'J':
            char_list = [char for char in char_list if char != char_list[i]]
    return ''.join(char_list)