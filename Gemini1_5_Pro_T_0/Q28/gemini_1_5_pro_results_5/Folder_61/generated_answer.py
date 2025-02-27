def return_nth_smallest_ascii(s):
    return sorted(list(set([c for i, c in enumerate(s) if i <= 9])))[9]