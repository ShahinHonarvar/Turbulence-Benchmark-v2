def return_nth_smallest_ascii(s):
    subset = [c for i, c in enumerate(s) if 48 <= i <= 76]
    sorted_subset = sorted(subset, key=lambda c: ord(c))
    return sorted_subset[4] if len(sorted_subset) >= 5 else None