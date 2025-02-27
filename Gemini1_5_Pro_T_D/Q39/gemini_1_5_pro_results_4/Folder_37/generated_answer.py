def return_n_greatest_chars(text):
    return sorted([ord(char) for char in text], reverse=True)[:26]