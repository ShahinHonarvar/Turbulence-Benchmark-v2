def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(8, 27)]
    asc_values = sorted([ord(c) for c in chars])
    sixth_smallest = asc_values[5]
    for c in chars:
        if ord(c) == sixth_smallest:
            return c