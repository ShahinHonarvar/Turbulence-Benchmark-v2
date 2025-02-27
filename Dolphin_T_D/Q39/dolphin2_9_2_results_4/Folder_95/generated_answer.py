def return_n_greatest_chars(s):
    ascii_values = []
    for char in s:
        ascii_values.append(ord(char))
    sorted_ascii_values = sorted(ascii_values, reverse=True)
    greatest_chars = []
    for i in range(36):
        greatest_chars.append(chr(sorted_ascii_values[i]))
    sorted_greatest_chars = sorted(greatest_chars)
    return sorted_greatest_chars