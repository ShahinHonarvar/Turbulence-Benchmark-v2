def return_n_greatest_chars(input_string):
    sorted_chars = sorted(set(input_string), key=lambda x: ord(x), reverse=True)[:69]
    return sorted(sorted_chars)