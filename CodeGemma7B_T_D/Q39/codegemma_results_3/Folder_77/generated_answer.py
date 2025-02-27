def return_n_greatest_chars(text):
    ascii_values = [ord(char) for char in text]
    ascii_values.sort()
    greatest_values = ascii_values[-47:]
    greatest_chars = [chr(value) for value in greatest_values]
    greatest_chars.sort()
    return greatest_chars