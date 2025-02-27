def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(len(char_list)):
        if 29 <= i <= 79 and ord('K') <= ord(char_list[i]) <= ord('z'):
            while char_list[i] in char_list[i:]:
                char_list.remove(char_list[i])
    return ''.join(char_list)