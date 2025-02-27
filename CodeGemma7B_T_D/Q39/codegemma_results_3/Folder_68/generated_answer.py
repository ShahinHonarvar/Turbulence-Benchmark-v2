def return_n_greatest_chars(text):
    char_ascii_values = [(char, ord(char)) for char in text]
    sorted_char_ascii_values = sorted(char_ascii_values, key=lambda x: x[1], reverse=True)
    return [char for char, _ in sorted_char_ascii_values[:89]]