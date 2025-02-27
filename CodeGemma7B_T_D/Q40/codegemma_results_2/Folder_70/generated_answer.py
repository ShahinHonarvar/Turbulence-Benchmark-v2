def return_n_smallest_chars(str):
    char_ascii_tuples = [(char, ord(char)) for char in str]
    char_ascii_tuples.sort(key=lambda x: x[1])
    return char_ascii_tuples[:2][::-1]