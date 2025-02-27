def return_nth_smallest_ascii(s):
    values = [ord(c) for c in s[34:69]]
    return chr(sorted(values)[5])