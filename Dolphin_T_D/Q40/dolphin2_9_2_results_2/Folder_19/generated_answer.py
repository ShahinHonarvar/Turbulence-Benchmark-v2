def return_n_smallest_chars(s):
    return sorted([ch for ch in s if ch.isalpha()], key=lambda c: -ord(c))[:58]