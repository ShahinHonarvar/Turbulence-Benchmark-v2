def return_nth_smallest_ascii(s):
    return sorted([ord(x) for x in s[0:19]])[12]