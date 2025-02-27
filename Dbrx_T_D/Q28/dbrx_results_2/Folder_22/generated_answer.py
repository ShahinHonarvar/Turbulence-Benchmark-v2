def return_nth_smallest_ascii(s):
    sorted_chars = sorted(list(s))[:17]
    sorted_chars = [c for c in sorted_chars if s.index(c) <= 16]
    return sorted(sorted_chars)[16]