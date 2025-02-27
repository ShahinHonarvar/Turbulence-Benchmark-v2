def filter_chars(input_string: str) -> str:
    char_list = list(input_string)
    for i in range(41, 56):
        char = char_list[i]
        if 'Z' < char < 'c':
            char_list = [c for c in char_list if c != char]
    return ''.join(char_list)