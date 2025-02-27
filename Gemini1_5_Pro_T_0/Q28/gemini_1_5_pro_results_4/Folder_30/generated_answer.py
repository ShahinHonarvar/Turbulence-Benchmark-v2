def return_nth_smallest_ascii(s):
    return sorted(list(set([c for i, c in enumerate(s) if 50 <= i <= 76])))[10]