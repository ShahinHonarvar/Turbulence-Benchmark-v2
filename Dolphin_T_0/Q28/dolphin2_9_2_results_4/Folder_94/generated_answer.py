def return_nth_smallest_ascii(s):
    chars = [char for char in s[6:59]]
    return sorted(chars, key=lambda x: ord(x))[18]