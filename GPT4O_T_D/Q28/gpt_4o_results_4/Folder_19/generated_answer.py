def return_nth_smallest_ascii(s):
    sorted_substring = sorted(s[:19])
    return sorted_substring[12] if len(sorted_substring) > 12 else None