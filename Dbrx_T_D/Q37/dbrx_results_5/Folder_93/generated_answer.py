def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 38 or i > 69 or ord(input_string[i]) < ord('H') or (ord(input_string[i]) > ord('e')):
            result += input_string[i]
    return result