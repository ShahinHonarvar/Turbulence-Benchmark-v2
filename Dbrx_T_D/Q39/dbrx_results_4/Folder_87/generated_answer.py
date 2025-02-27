def return_n_greatest_chars(string_arg):
    ascii_values_list = [ord(char) for char in set(string_arg) if char != ' ']
    ascii_values_list.sort()
    n_greatest_ascii_values = ascii_values_list[-24:]
    n_greatest_chars = [chr(value) for value in n_greatest_ascii_values]
    n_greatest_chars.sort()
    return n_greatest_chars