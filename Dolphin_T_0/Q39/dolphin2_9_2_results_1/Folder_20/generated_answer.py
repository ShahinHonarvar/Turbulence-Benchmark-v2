def return_n_greatest_chars(s):
    chars = sorted([c for c in s for _ in range(40)], reverse=True)
    chars.sort()
    return chars