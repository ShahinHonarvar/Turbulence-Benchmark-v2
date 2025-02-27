def return_n_smallest_chars(s):
    return sorted([char for char in s], key=lambda x: x.encode('utf-8')[0])[:45][::-1]