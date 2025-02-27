def return_nth_smallest_ascii(s):
    return sorted(s[:7], key=lambda x: ord(x))[6]