def return_n_smallest_chars(s):
    return sorted([_ for _ in s] * (72 // len(s) + 1), key=lambda x: -ord(x))[:72]