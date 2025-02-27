def return_n_greatest_chars(string):
    greatest_chars = sorted([char for char in string], reverse=True)
    greatest_chars = greatest_chars[:23]
    greatest_chars.sort()
    return greatest_chars