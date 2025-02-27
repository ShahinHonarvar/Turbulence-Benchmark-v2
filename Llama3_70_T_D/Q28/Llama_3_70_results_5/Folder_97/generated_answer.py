def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(15, 22)]
    return sorted(chars, key=ord)[5]