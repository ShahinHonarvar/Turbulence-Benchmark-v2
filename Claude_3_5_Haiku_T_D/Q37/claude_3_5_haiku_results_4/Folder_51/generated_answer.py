def filter_chars(input_string):
    result = []
    for i, char in enumerate(input_string):
        if 36 <= i <= 40 and 'H' <= char <= 'e':
            result.extend([c for c in input_string if c != char])
            return ''.join(result)
    return input_string