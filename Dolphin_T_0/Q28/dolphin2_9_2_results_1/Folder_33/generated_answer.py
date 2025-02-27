def return_nth_smallest_ascii(s):
    values = [ord(c) for i, c in enumerate(s) if 22 <= i <= 74]
    return chr(sorted(values)[11])