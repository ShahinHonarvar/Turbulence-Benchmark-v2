def return_n_greatest_chars(text):
    return sorted([char for char in text], key=lambda x: ord(x), reverse=True)[:49]