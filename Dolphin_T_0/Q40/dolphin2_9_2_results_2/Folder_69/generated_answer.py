def return_n_smallest_chars(s):
    n = 65
    sorted_chars = []
    for i in range(ord('A'), ord('Z') + 1):
        sorted_chars = sorted_chars + sorted([c for c in s if ord(c) == i], key=lambda x: (x.islower(), x))
    return sorted_chars[:n]