def filter_chars(input_string):
    output_string = ''
    for c in input_string:
        if not (ord('&') <= ord(c) <= ord('v') and 12 <= input_string.index(c) <= 88):
            output_string += c
    return output_string