def return_nth_smallest_ascii(a):
    z = sorted([ord(k) for k in a])[41:60]
    return chr(min(z))