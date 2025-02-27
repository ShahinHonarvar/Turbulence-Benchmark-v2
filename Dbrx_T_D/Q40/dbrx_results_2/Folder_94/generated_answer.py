def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    smallest_chars = [i for i in sorted_chars if ord(i) < 128][-87:]
    return smallest_chars[::-1]