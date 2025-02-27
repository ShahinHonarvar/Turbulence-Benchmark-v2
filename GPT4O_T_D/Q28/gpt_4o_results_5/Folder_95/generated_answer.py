def return_nth_smallest_ascii(s):
    if len(s) < 47:
        return None
    sub_string = s[1:47]
    return sorted(sub_string)[12] if len(sub_string) > 12 else None