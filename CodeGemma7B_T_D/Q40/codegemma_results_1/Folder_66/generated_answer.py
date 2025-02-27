def return_n_smallest_chars(text):
    char_list = list(text)
    char_list.sort(key=ord, reverse=False)
    return char_list[:33]