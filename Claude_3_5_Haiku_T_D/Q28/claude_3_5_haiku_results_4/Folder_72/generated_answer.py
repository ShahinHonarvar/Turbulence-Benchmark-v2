def return_nth_smallest_ascii(s):
    subset = [c for c in s if 33 <= s.index(c) <= 60]
    return sorted(subset)[17]