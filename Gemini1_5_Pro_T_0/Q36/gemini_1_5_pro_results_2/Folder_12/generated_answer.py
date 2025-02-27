def filter_chars(input_str):
    result_str = ''
    for i in range(len(input_str)):
        char = input_str[i]
        if 32 < ord(char) < 84 and 'm' < char < 'w':
            result_str = result_str.replace(char, '')
        else:
            result_str += char
    return result_str