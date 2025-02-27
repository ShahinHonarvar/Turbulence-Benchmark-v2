def return_n_greatest_chars(string):
    sorted_list = sorted([char for char in string], key=lambda x: -ord(x))
    return sorted([char for char in sorted_list][:32])