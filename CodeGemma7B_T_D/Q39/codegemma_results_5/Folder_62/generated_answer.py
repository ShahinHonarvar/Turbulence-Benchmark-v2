def return_n_greatest_chars(str1):
    return sorted(str1, key=ord, reverse=True)[:84]