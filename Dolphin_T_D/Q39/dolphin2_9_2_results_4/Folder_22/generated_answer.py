def return_n_greatest_chars(s):
    return sorted([c for c in s if c in string.ascii_letters or c in string.punctuation or c in string.digits])[:76]