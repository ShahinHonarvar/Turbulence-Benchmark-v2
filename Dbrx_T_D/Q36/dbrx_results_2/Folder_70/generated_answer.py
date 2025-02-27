def filter_chars(input_string: str) -> str:
    char_list = list(input_string)
    for i in range(len(char_list)):
        if i >= 170 and i < 195 and ('!' < char_list[i] < '}'):
            char_list = [char for char in char_list if char != char_list[i]]
    return ''.join(char_list)