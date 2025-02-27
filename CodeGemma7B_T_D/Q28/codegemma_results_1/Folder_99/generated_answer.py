def return_nth_smallest_ascii(str):
    existing = list(str)
    existing.sort(key=lambda c: ord(c))
    return existing[8]