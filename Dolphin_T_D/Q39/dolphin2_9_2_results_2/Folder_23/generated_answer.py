def return_n_greatest_chars(string):
    string_list = list(string)
    sorted_list = sorted(string_list)
    greatest_chars = sorted_list[:-47:-1]
    result = sorted(greatest_chars)
    return result