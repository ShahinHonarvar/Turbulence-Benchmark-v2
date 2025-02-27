def return_nth_smallest_ascii(s):
    candidates = [c for i, c in enumerate(s) if 48 <= i <= 76]
    candidates.sort(key=lambda x: ord(x))
    return candidates[4]