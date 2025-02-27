def return_nth_smallest_ascii(s):
    distinct_chars = sorted(set(s[18:46]))
    return distinct_chars[6] if len(distinct_chars) >= 7 else None