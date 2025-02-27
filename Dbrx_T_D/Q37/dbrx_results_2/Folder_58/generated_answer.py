def filter_chars(input_string):
    char_list = list(input_string)
    filtered_chars = []
    for i in range(len(char_list)):
        if i < 503 or i > 753:
            filtered_chars.append(char_list[i])
        elif char_list[i] < '9' or char_list[i] > 'w':
            filtered_chars.append(char_list[i])
    return ''.join(filtered_chars)