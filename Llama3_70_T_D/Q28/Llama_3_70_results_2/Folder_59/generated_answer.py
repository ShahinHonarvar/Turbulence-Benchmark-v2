def return_nth_smallest_ascii(s):
    if len(s) < 12:
        return None
    else:
        return sorted(s[:12])[11]