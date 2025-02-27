def return_n_greatest_chars(input_str):
    sorted_list = sorted([char for char in input_str], key=lambda x: -ord(x))
    return sorted_list[:90]