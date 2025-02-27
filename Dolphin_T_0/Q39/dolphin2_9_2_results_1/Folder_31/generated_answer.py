def return_n_greatest_chars(input_string):
    chars = [char for char in input_string if char.isalpha()]
    chars.sort(key=lambda x: -ord(x))
    return chars[:70]