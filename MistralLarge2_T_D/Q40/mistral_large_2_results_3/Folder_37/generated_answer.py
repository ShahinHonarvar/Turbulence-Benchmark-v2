def return_n_smallest_chars(s):
    return sorted([c for c in s if len(set(s)) >= 26], key=lambda x: -ord(x))[:26]