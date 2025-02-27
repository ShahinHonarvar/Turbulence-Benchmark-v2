def return_n_greatest_chars(string):
    greatest = sorted(string, key=ord, reverse=True)[:73]
    greatest.sort()
    return greatest