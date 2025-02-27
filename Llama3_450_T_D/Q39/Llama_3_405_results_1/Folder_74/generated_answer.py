def return_n_greatest_chars(s):
    ascii_values = [(char, ord(char)) for char in s]
    ascii_values.sort(key=lambda x: x[1], reverse=True)
    greatest_chars = [char for char, _ in ascii_values[:5]]
    greatest_chars.sort()
    return greatest_chars