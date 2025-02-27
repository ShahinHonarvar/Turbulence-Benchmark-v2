def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    ascii_list.sort(reverse=True)
    n_greatest_chars = [chr(ascii) for ascii in ascii_list[:61]]
    return n_greatest_chars