def return_n_greatest_chars(input_str):
    list = sorted(input_str, key=ord, reverse=True)
    n_greatest = list[:5]
    return n_greatest