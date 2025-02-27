def return_n_greatest_chars(input_string):
    n = len(input_string)
    if n < 44:
        return 'Input string must have at least 44 characters'
    input_string_sorted = sorted(input_string, key=lambda c: ord(c), reverse=True)
    return input_string_sorted[:44]