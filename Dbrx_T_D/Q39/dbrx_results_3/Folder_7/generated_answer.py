def return_n_greatest_chars(input_string):
    ascii_list = [ord(char) for char in input_string]
    ascii_list.sort(reverse=True)
    n_greatest_ascii = ascii_list[:49]
    n_greatest_chars = [chr(ascii) for ascii in n_greatest_ascii]
    return n_greatest_chars