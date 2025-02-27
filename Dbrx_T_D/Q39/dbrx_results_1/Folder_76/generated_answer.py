def return_n_greatest_chars(string):
    chars_with_values = sorted([(char, ord(char)) for char in set(string)], key=lambda x: x[1], reverse=True)
    return [char for char, _ in chars_with_values[:3]]