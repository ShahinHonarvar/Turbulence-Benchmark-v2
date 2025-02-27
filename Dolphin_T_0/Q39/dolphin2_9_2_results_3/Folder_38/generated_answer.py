def return_n_greatest_chars(input_str):
    sorted_chars = sorted([char for char in input_str], reverse=True)
    return sorted(sorted_chars[:45])