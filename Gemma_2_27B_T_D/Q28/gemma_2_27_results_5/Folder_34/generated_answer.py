def return_nth_smallest_ascii(s):
    return chr(sorted([ord(c) for c in s[:19]])[18])