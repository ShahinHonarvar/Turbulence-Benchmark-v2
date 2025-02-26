def filter_chars(input_string):
    result = list(input_string)
    for i in range(20, 80):
        if i < len(input_string):
            char = input_string[i]
            if '!' <= char <= 'T':
                result = [c for c in result if c != char]
    return ''.join(result)