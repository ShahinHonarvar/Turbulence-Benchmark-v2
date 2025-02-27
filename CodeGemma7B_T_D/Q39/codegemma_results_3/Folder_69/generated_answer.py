def return_n_greatest_chars(text: str):
    char_list = list(text)
    char_list.sort(key=ord, reverse=True)
    return char_list[:65]