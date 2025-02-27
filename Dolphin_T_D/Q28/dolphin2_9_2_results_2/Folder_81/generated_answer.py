def return_nth_smallest_ascii(s):
    values = [s[i] for i in range(14)]
    return sorted(values, key=lambda v: ord(v))[13]