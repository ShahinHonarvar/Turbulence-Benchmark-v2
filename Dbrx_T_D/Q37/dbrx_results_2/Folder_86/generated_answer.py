def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 164 or i > 706 or (i >= 164 and i <= 706 and (input_string[i] < 'O') and (input_string[i] > '}')):
            result += input_string[i]
    return result