def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 27 or i >= 75:
            result += input_string[i]
        elif ord('A') < ord(input_string[i]) and ord(input_string[i]) < ord('i'):
            result += input_string[i]
    return result