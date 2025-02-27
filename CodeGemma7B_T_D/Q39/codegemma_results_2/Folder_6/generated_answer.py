def return_n_greatest_chars(str1):
    return sorted([i for i in str1], key=ord, reverse=True)[:47]