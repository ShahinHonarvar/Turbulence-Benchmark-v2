def return_n_greatest_chars(input_str):
    sorted_str = sorted(input_str, key=lambda x: ord(x), reverse=True)
    return sorted_str[:66]