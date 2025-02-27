def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 63 or i > 84 or ord(input_string[i]) < ord('E') or (ord(input_string[i]) > ord('~')):
            result += input_string[i]
    return result