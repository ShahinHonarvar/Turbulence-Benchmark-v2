def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 10 or i > 69 or ord(input_string[i]) < ord('I') or (ord(input_string[i]) > ord('K')):
            result += input_string[i]
    return result