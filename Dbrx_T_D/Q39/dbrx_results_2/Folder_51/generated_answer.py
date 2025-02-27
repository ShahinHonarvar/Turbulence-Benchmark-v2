def return_n_greatest_chars(string_of_chars):
    ascii_chars = [ord(char) for char in set(string_of_chars)]
    ascii_chars.sort(reverse=True)
    greatest_45_chars = [chr(ascii) for ascii in ascii_chars[:45]]
    return greatest_45_chars