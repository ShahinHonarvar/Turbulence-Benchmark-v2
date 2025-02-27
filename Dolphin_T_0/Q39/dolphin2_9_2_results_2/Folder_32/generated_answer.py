def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(reverse=True)
    greatest_chars = chars[:8]
    greatest_chars.sort()
    return greatest_chars