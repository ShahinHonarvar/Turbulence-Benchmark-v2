def return_n_smallest_chars(s):
    return sorted(sorted(s, key=lambda x: ord(x))[:37], reverse=True)