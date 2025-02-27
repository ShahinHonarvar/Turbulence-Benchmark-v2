def return_n_greatest_chars(charStr):
    return sorted(charStr, key=ord, reverse=True)[:33]