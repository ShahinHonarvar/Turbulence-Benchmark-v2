def return_nth_smallest_ascii(text):
    return sorted(list(set([c for i, c in enumerate(text) if i >= 20 and i <= 30])))[7]