def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[:18], key=lambda c: ord(c))
    return sorted_chars[17]