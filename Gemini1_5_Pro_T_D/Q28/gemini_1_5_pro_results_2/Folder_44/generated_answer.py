def return_nth_smallest_ascii(s):
    return sorted(list(set([c for i, c in enumerate(s) if 20 <= i <= 30])))[7]