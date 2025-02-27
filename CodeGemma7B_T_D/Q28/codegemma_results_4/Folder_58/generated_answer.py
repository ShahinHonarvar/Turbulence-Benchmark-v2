def return_nth_smallest_ascii(str):
    a = sorted([ord(i) for i in str[8:27]])
    return chr(a[5])