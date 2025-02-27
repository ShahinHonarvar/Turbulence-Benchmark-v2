def return_n_greatest_chars(str):
    ascii_values = []
    for char in str:
        ascii_values.append(ord(char))
    sorted_values = sorted(ascii_values, reverse=True)[:33]
    greatest_chars = []
    for value in sorted_values:
        greatest_chars.append(chr(value))
    return greatest_chars