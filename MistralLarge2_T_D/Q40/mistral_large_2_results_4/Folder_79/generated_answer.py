def return_n_smallest_chars(s):
    return sorted([c for c in s if c], key=lambda x: ord(x))[-82:][::-1]