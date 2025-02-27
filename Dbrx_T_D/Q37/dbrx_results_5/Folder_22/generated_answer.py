def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if 33 <= i <= 70:
            char = input_string[i]
            if not '7' <= char <= 'k':
                result += char
        else:
            result += input_string[i]
    return result