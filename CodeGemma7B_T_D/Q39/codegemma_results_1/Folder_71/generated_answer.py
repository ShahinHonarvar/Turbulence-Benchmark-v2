def return_n_greatest_chars(text):
    text_list = list(text)
    text_list.sort(key=ord, reverse=True)
    return text_list[:14]