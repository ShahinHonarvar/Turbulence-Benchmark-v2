def return_n_greatest_chars(text):
    ascii_values = []
    for char in text:
        ascii_values.append((ord(char), char))
    ascii_values.sort(reverse=True)
    return [char for _, char in ascii_values[:35]]