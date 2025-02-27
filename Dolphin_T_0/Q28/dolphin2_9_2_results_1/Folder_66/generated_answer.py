def return_nth_smallest_ascii(s):
    substring = s[35:53]
    ascii_values = [ord(ch) for ch in substring]
    nth_smallest = sorted(ascii_values)[9]
    for ch in substring:
        if ord(ch) == nth_smallest:
            return ch