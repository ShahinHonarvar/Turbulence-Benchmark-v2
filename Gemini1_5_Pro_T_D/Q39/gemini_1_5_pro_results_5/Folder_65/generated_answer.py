def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) <= 122 and ord(c) >= 97], reverse=True)[:27]