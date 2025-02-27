def return_n_smallest_chars(input_str):
    input_str = list(input_str)
    sorted_str = sorted(input_str, key=lambda x: ord(x))
    return sorted_str[:37]