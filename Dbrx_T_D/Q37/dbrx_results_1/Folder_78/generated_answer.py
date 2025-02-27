def filter_chars(input_string):
    char_list = list(input_string)
    filtered_list = []
    for i in range(len(char_list)):
        if i < 75 or i > 99:
            filtered_list.append(char_list[i])
        elif char_list[i] < '8' or char_list[i] > 'e':
            filtered_list.append(char_list[i])
    return ''.join(filtered_list)