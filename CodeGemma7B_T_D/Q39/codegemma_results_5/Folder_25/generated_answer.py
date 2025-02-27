def return_n_greatest_chars(text):
    ascii_values = []
    greatest_chars = []
    for char in text:
        ascii_values.append(ord(char))
    ascii_values.sort(reverse=True)
    for value in ascii_values[:29]:
        greatest_chars.append(chr(value))
    return greatest_chars