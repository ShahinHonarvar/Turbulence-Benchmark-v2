def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 33 or i > 70 or (ord(input_string[i]) < 55 and ord(input_string[i]) > 107):
            result += input_string[i]
    return result