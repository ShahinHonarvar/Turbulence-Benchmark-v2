def return_n_smallest_chars(s):
    smallest = sorted(s)[:2]
    smallest.sort(reverse=True)
    return smallest