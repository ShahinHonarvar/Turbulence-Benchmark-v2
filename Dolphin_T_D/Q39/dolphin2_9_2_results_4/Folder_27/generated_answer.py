def return_n_greatest_chars(s):
    s = list(s)
    length = len(s)
    if length < 82:
        return []
    s.sort()
    n_greatest = []
    for _ in range(82):
        n_greatest.append(s.pop())
    return n_greatest