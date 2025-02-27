def return_n_smallest_chars(test_string):
    n = 88
    smallest_chars = sorted(test_string, key=lambda x: ord(x))[:n]
    smallest_chars.sort(reverse=True)
    return smallest_chars