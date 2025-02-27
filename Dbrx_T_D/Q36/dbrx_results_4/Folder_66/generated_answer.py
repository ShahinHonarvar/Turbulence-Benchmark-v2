def filter_chars(input_string: str) -> str:
    char_list = list(input_string)
    for i in range(39, 87):
        if '!' < char_list[i] < '}':
            char_list = [char for char in char_list if char != char_list[i]]
    return ''.join(char_list)