def filter_chars(input_string):
    result = []
    for i, char in enumerate(input_string):
        if 50 < i < 92 and 'A' < char < 'Q':
            result.extend([c for c in input_string if c != char])
            return ''.join(result)
    return input_string