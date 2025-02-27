def return_nth_smallest_ascii(s):
    subset = [c for c in s if 0 <= s.index(c) <= 16]
    subset.sort(key=ord)
    return subset[16] if len(subset) > 16 else None