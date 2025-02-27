def return_n_greatest_chars(string):
    return sorted(string, key=ord, reverse=True)[:int(len(string) / 13)]