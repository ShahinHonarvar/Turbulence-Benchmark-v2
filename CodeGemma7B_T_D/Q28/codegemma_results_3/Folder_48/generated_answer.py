def return_nth_smallest_ascii(string):
    A = sorted([ord(c) for c in string[37:60]])
    return chr(A[5])