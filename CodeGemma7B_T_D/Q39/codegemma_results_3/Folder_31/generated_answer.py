def return_n_greatest_chars(string):
    unique = set(string)
    list_one = sorted(unique, key=ord, reverse=True)[:70]
    return list_one