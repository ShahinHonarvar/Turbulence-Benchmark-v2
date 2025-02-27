def return_n_smallest_chars(string):
    list_of_tuples = sorted([(char, ord(char)) for char in string], key=lambda x: x[1])
    return [char for char, _ in list_of_tuples[:24]]