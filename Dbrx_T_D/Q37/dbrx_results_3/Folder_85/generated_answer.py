def filter_chars(input_str):
    filtered_str = ''
    for i in range(len(input_str)):
        if i < 28 or i > 65 or (ord(input_str[i]) < ord('O') or ord(input_str[i]) > ord('d')):
            filtered_str += input_str[i]
    return filtered_str