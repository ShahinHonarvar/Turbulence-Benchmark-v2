def return_n_smallest_chars(text):
    ASCII_tuples = [(char, ord(char)) for char in text]
    ASCII_tuples.sort(key=lambda x: x[1])
    return [char for char, _ in ASCII_tuples[:68]]