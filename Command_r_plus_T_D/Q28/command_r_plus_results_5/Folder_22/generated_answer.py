def return_nth_smallest_ascii(s):
    s = s[:17]
    return min(s, key=lambda x: ord(x))