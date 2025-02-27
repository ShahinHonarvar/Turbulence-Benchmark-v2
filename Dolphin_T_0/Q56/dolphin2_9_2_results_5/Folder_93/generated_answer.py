def all_substring_of_size_n(n):
    return [s for s in n.split() if len(set(s)) == len(s) and len(s) == 54]