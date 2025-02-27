def return_n_smallest_chars(chars):
    list_of_tuples = [(char, ord(char)) for char in chars]
    list_of_tuples.sort(key=lambda x: x[1], reverse=True)
    return [char for char, _ in list_of_tuples[:72]]