def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(len(char_list)):
        if 24 < i < 37 and 'A' < char_list[i] < 'h':
            while char_list[i] in char_list:
                char_list.remove(char_list[i])
            i -= 1
    return ''.join(char_list)