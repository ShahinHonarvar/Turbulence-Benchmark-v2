def filter_chars(input_string):
    filtered_string = ''.join((c for c in input_string if not (323 < input_string.index(c) < 526 and ')' < c < 'O' and (c in input_string[324:526]))))
    return filtered_string