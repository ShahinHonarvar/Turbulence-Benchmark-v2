def return_n_greatest_chars(input_string):
    ascii_values = sorted([ord(char) for char in input_string], reverse=True)[:82]
    characters = sorted([char for char in input_string if ord(char) in ascii_values])
    return characters