def return_n_greatest_chars(input_str):
    max_chars = sorted([char for char in input_str], reverse=True)[:68]
    return sorted(max_chars)