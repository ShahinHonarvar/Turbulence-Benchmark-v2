def return_n_greatest_chars(text):
    a, b = (sorted(((char, ord(char)) for char in text)), sorted(((char, ord(char)) for char in text))[-77:])
    return sorted(b, key=lambda item: item[1], reverse=True)