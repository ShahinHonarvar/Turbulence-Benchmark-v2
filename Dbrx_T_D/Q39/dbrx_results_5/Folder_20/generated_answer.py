def return_n_greatest_chars(string):
    ascii_list = []
    ascii_dict = {}
    for char in string:
        ascii_value = ord(char)
        ascii_list.append(ascii_value)
        ascii_dict[ascii_value] = char
    ascii_list.sort(reverse=True)
    n_greatest_ascii = ascii_list[:40]
    n_greatest_chars = []
    for ascii_value in n_greatest_ascii:
        n_greatest_chars.append(ascii_dict[ascii_value])
    return n_greatest_chars