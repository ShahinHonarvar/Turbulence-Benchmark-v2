def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=lambda x: (x.isalpha(), x))[84:]
    return sorted(smallest_chars, reverse=True)