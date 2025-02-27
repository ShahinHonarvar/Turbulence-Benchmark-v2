def return_n_greatest_chars(text):
    return sorted([x for x in text if ord(x) <= 122 and ord(x) >= 97], reverse=True)[:26]