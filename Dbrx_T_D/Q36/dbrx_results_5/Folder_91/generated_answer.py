def filter_chars(input_string: str) -> str:
    char_list = list(input_string)
    for i in range(len(char_list)):
        if '0' <= char_list[i] <= '9' or 'A' <= char_list[i] <= 'Z' or 'a' <= char_list[i] <= 'z':
            continue
        if '$' < char_list[i] < '?' and i >= 0 and (i < 3):
            while char_list[i] in input_string:
                input_string = input_string.replace(char_list[i], '', 1)
    return input_string