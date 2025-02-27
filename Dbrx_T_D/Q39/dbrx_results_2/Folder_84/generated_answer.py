def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    sorted_ascii_list = sorted(ascii_list)[-10:]
    return [chr(num) for num in sorted_ascii_list]