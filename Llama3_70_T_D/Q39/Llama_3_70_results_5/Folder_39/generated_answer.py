def return_n_greatest_chars(char_string):
    char_string = list(char_string)
    char_string.sort(reverse=True)
    n_greatest_chars = sorted(char_string[:23])
    return n_greatest_chars