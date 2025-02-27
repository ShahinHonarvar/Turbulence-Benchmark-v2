def return_n_smallest_chars(inp):
    return sorted([c for c in inp], key=lambda c: ord(c), reverse=True)[:21]