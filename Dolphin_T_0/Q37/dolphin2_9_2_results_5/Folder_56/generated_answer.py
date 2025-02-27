def filter_chars(input_string):
    new_string = ''
    for i in range(len(input_string)):
        if i >= 71 and i <= 94:
            ch = input_string[i]
            if ch >= 'K' and ch <= 'a':
                continue
        new_string += input_string[i]
    return new_string