def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 41 or i > 79 or ord(input_string[i]) < ord('f') or (ord(input_string[i]) > ord('|')):
            result += input_string[i]
    return result