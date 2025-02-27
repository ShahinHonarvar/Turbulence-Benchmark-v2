def filter_chars(input_str):
    result = ''
    for i in range(len(input_str)):
        if i < 58 or i > 81:
            result += input_str[i]
        elif input_str[i] > 'F' and input_str[i] < 'O':
            result += input_str[i]
    return result