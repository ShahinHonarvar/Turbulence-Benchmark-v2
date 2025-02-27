def filter_chars(input_string: str) -> str:
    char_list = list(input_string)
    filtered_list = []
    for i in range(len(char_list)):
        if i < 43 or i > 80:
            filtered_list.append(char_list[i])
        elif ord(char_list[i]) >= ord('=') and ord(char_list[i]) <= ord('E'):
            continue
        else:
            filtered_list.append(char_list[i])
    return ''.join(filtered_list)