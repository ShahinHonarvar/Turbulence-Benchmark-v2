def return_n_smallest_chars(input_string):
    return sorted([char for char in input_string], key=lambda x: ord(x), reverse=True)[:45]