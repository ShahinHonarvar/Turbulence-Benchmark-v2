def return_nth_smallest_ascii(s):
    return sorted([ord(c) for c in s[:70]])[9]