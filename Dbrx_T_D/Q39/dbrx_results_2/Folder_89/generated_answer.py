def return_n_greatest_chars(input_string):
    ascii_list = [ord(char) for char in input_string]
    ascii_list.sort(reverse=True)
    n_greatest_chars = [chr(char) for char in ascii_list[:55]]
    return n_greatest_chars