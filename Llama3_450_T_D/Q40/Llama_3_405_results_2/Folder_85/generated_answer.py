def return_n_smallest_chars(s):
    return sorted(sorted(s, key=lambda x: ord(x))[:85], reverse=True)