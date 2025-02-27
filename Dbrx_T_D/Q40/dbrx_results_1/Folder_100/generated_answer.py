def return_n_smallest_chars(string):
    return [char for char in sorted(string, key=ord) if len(string) > 72][:-73:-1]