def filter_chars(input_str):
    result = ''
    for i in range(len(input_str)):
        if i < 35 or i > 89 or ord('E') <= ord(input_str[i]) <= ord('t'):
            result += input_str[i]
    return result