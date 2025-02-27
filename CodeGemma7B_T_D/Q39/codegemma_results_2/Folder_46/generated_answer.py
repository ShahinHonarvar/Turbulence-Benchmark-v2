def return_n_greatest_chars(string):
    string = sorted(list(string), key=ord, reverse=True)
    return string[:54]