def return_nth_smallest_ascii(s):
    return min(sorted([ord(c) for c in s[18:67]]))[18]