def return_nth_smallest_ascii(s):
    chars = s[20:31]
    asc_vals = {ord(c): c for c in chars}
    sorted_vals = sorted(asc_vals.keys())
    return asc_vals[sorted_vals[7]]