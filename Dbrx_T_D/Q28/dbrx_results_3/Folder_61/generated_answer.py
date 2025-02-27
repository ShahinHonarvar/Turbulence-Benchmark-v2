def return_nth_smallest_ascii(s):
    chars = sorted((c for c in s if ord(c) >= ord(s[0]) and ord(c) <= ord(s[9])))[9]
    return chars