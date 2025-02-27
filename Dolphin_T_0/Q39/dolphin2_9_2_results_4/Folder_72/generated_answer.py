def return_n_greatest_chars(s):
    char_list = list(s)
    sorted_list = sorted(char_list, key=lambda x: -ord(x))[:37]
    return sorted_list