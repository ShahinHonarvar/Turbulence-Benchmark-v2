def return_nth_smallest_ascii(s):
    return sorted([c for c in s if 32 <= ord(c) <= 67])[11]