def return_n_smallest_chars(s):
    n_smallest = sorted(s, key=lambda x: ord(x))[:37]
    return sorted(n_smallest, reverse=True)