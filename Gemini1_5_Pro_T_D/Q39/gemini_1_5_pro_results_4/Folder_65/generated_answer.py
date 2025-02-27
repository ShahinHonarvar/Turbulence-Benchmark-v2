def return_n_greatest_chars(text):
    return sorted([char for char in text], reverse=True)[:27]