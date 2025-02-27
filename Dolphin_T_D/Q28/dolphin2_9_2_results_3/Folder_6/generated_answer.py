def return_nth_smallest_ascii(s):
    vals = {ord(c): c for c in s[14:55]}
    sorted_vals = sorted(vals.keys())
    return vals[sorted_vals[10]]