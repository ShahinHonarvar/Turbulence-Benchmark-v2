def return_n_greatest_chars(input_str):
    ascii_chars = [ord(char) for char in input_str if input_str.count(char) == 1]
    sorted_ascii_chars = sorted(ascii_chars)[-36:]
    return [chr(char) for char in sorted_ascii_chars]