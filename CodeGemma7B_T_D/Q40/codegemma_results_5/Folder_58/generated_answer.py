def return_n_smallest_chars(string):
    list = [char for char in string]
    list.sort(key=str.ascii_value, reverse=True)
    return list[:49]