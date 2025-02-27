def return_nth_smallest_ascii(s):
    s_slice = s[34:69]
    asc_values = sorted([ord(c) for c in s_slice])
    sixth_smallest = asc_values[5]
    for c in s_slice:
        if ord(c) == sixth_smallest:
            return c