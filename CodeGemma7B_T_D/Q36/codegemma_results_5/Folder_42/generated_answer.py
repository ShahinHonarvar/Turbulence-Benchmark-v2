def filter_chars(str_input):
    for i in range(42, 68):
        if str_input[i] > 't' and str_input[i] < 'x':
            while str_input[i] in str_input:
                str_input = str_input.replace(str_input[i], '')
    return str_input