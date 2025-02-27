def filter_chars(input_str):
    result_str = ''
    for i in range(len(input_str)):
        if i >= 15 and i < 85:
            if ord('I') < ord(input_str[i]) < ord('M'):
                continue
        result_str += input_str[i]
    return result_str