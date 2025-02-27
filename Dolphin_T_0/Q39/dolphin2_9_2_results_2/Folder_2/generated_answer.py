def return_n_greatest_chars(input_string):
    greatest_chars_sorted = sorted([char for char in input_string], reverse=True)[:48]
    greatest_chars_sorted.sort()
    return greatest_chars_sorted