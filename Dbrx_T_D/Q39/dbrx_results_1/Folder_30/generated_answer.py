def return_n_greatest_chars(input_string):
    ascii_chars = [char for char in input_string if ord(char) >= 32 and ord(char) <= 126]
    sorted_chars = sorted(ascii_chars)[:72]
    return sorted_chars