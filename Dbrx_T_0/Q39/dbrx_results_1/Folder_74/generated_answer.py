def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    ascii_list.sort(reverse=True)
    n_greatest = ascii_list[:5]
    result = [chr(ascii) for ascii in n_greatest]
    return result