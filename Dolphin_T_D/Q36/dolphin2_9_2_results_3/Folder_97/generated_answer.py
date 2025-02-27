def filter_chars(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < 309 or i >= 591:
            result += input_string[i]
        elif input_string[i] > 'S' and input_string[i] < 'm':
            input_string = input_string.replace(input_string[i], '')
    return result