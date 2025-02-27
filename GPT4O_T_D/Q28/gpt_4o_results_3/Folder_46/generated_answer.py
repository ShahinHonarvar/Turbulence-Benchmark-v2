def return_nth_smallest_ascii(s):
    if len(s) < 86:
        return None
    return sorted(s[34:86])[19] if len(s[34:86]) >= 20 else None