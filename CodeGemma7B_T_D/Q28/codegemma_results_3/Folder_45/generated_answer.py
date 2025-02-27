def return_nth_smallest_ascii(arr):
    return sorted([ord(i) for i in arr])[15]