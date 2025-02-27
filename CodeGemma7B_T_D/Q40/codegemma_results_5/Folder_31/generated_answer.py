def return_n_smallest_chars(text):
    ASCII_codes = [ord(char) for char in text]
    ascii_tuples = list(zip(ASCII_codes, text))
    ascii_tuples.sort(key=lambda x: x[1])
    ascii_tuples = ascii_tuples[:70]
    return [char for code, char in ascii_tuples]