def return_n_smallest_chars(s):
    return sorted(sorted(s, key=lambda x: ord(x))[:88], reverse=True)