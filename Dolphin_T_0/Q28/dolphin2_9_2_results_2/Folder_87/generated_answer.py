def return_nth_smallest_ascii(s):
    substring = s[29:34]
    ascii_values = [ord(c) for c in substring]
    fifth_smallest = sorted(ascii_values)[4]
    for c in substring:
        if ord(c) == fifth_smallest:
            return c