def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if 7 <= i <= 9 and ord('6') <= ord(input_string[i]) and (ord(input_string[i]) <= ord('w')):
            continue
        else:
            result_string += input_string[i]
    return result_string