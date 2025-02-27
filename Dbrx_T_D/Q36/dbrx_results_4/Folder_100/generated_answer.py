def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(len(char_list)):
        if 43 < i < 69 and char_list[i] > 'B' and (char_list[i] < 'r'):
            while char_list[i] in char_list:
                char_list.remove(char_list[i])
    return ''.join(char_list)