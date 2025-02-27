def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= 521 and i <= 722:
            if ord(input_string[i]) >= ord('>') and ord(input_string[i]) <= ord('_'):
                continue
        filtered_string += input_string[i]
    return filtered_string