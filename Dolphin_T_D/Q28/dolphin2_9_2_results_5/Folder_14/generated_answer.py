def return_nth_smallest_ascii(s):
    ascii_vals = [ord(c) for c in s[46:83]]
    ascii_vals.sort()
    target_val = ascii_vals[15]
    for c in s[46:83]:
        if ord(c) == target_val:
            return c