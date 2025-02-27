def return_n_greatest_chars(input_string):
    sorted_string = sorted([char for char in input_string], reverse=True)
    return sorted_string[:27]