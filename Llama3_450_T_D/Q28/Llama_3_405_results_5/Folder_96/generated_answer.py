def return_nth_smallest_ascii(s):
    return sorted(s[:18], key=lambda c: ord(c))[17]