def return_n_smallest_chars(str):
    list = sorted([char for char in str], key=ord, reverse=False)[:11]
    return list[::-1]