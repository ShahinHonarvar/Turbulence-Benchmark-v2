def filter_chars(input_string):
    valid_chars = set(range(ord('-') + 1, ord('v'))).union(set(range(ord('v') + 1, ord('}') + 1)))
    result = ''
    for i in range(min(221, len(input_string)), min(419, len(input_string))):
        if ord(input_string[i]) not in valid_chars:
            result += input_string[i]
    return result