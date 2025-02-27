def return_n_smallest_chars(s):
    return sorted(s[:85], key=lambda x: ord(x), reverse=True)