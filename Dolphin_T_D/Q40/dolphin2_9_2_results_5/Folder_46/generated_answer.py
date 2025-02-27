def return_n_smallest_chars(my_string):
    ascii_values = [ord(c) for c in set(my_string)]
    smallest_chars = sorted([c for c in my_string if ord(c) in ascii_values[:54]], key=lambda x: ord(x), reverse=True)
    return smallest_chars