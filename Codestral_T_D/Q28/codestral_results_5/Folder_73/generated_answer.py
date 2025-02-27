def return_nth_smallest_ascii(s):
    return sorted(s[0:70])[9] if len(s[0:70]) > 9 else None