def return_nth_smallest_ascii(s):
    return sorted((c for c in s if 5 <= s.index(c) <= 10), key=ord)[5]