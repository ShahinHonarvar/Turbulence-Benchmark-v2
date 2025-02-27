def return_nth_smallest_ascii(s):
    sorted_chars = sorted(set(s[:12]))
    return sorted_chars[11]