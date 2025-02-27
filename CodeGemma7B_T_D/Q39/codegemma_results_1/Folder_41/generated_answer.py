def return_n_greatest_chars(string):
    list = sorted(string, key=ord, reverse=True)
    return list[:37]