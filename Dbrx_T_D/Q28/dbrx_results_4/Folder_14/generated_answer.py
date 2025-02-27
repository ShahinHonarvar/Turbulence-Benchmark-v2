def return_nth_smallest_ascii(input_string):
    chars_to_check = [char for char in input_string[46:83] if char.isascii() and char.islower()]
    chars_to_check.sort(key=lambda x: ord(x))
    return chars_to_check[15]