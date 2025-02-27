def filter_chars(s: str) -> str:
    char_list = list(s)
    for i in range(len(char_list)):
        if i >= 170 and i < 195:
            char = char_list[i]
            if '!' < char < '}':
                char_list = [j for j in char_list if j != char]
    return ''.join(char_list)