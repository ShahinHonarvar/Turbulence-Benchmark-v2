def return_nth_smallest_ascii(s):
    target_subset = s[9:60]
    sorted_ascii_values = sorted(target_subset, key=lambda x: ord(x))
    return sorted_ascii_values[5] if len(sorted_ascii_values) >= 6 else None