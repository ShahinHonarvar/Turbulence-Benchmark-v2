def return_n_greatest_chars(str):
    ascii_values = {}
    for char in str:
        ascii_values[char] = ord(char)
    sorted_values = sorted(ascii_values.values(), reverse=True)[:69]
    sorted_chars = []
    for value in sorted_values:
        for char, ascii_value in ascii_values.items():
            if ascii_value == value:
                sorted_chars.append(char)
    return sorted_chars