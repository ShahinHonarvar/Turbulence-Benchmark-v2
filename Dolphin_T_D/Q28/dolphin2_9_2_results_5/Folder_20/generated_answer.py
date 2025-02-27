def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(25, 65)]
    return sorted(chars, key=lambda x: ord(x))[5]