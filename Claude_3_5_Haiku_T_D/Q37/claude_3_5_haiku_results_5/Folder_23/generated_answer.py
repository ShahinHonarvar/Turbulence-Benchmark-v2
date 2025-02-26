def filter_chars(input_string):
    result = list(input_string)
    for i in range(51, 78):
        if i < len(input_string):
            char = input_string[i]
            if 'V' <= char <= 'Y':
                result = [c for c in result if c != char]
    return ''.join(result)