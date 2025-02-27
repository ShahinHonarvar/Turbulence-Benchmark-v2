def return_n_greatest_chars(s):
    sorted_list = sorted([char for char in s], reverse=True)
    return sorted_list[:35]