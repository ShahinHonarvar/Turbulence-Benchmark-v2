def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 57 or i > 96 or ord(input_string[i]) < ord('<') or (ord(input_string[i]) > ord('w')):
            result += input_string[i]
    return result