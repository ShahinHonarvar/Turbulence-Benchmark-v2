def return_nth_smallest_ascii(s):
    substring = s[0:70]
    asc_vals = [ord(c) for c in substring]
    asc_vals.sort()
    return chr(asc_vals[9])