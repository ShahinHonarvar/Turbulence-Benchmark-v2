def return_n_greatest_chars(input_string):
    character_ascii_values = sorted([(char, ord(char)) for char in input_string], key=lambda x: x[1], reverse=True)
    return [char for char, _ in character_ascii_values[:70]]