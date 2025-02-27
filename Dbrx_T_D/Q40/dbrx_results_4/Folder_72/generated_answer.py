def return_n_smallest_chars(input_string):
    input_list = sorted(list(set(input_string)), key=ord)[:37]
    return input_list[::-1]