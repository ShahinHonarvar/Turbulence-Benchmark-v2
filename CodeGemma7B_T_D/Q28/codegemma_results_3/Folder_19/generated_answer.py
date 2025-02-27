def return_nth_smallest_ascii(z):
    codes = [ord(c) for c in z[0:19]]
    codes.sort()
    return chr(codes[12])