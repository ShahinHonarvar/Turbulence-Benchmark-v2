def return_n_greatest_chars(text):
    text_list = list(text)
    sorted_list = sorted(text_list, key=lambda x: -ord(x))
    n_greatest = sorted_list[:47]
    sorted_list = sorted(n_greatest)
    return sorted_list