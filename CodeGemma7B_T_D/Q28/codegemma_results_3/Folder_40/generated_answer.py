def return_nth_smallest_ascii(s):
    return sorted((c for c in s if s.index(c) <= 4))[4]