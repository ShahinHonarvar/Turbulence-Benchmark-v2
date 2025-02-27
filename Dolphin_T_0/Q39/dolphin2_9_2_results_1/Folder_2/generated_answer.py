def return_n_greatest_chars(s):
    return sorted([char for char in s if char in string.ascii_letters or char in string.digits])[:48]