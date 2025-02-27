def return_n_greatest_chars(arg1):
    sorted_list = sorted(list(arg1), key=lambda x: -ord(x))
    return sorted_list[:89]