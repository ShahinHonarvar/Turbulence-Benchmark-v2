def return_nth_smallest_ascii(s):
    return sorted(s[:12], key=lambda x: ord(x))[11]