def return_nth_smallest_ascii(s):
    distinct_chars = sorted(set(s[:10]))
    return distinct_chars[9] if len(distinct_chars) >= 10 else None