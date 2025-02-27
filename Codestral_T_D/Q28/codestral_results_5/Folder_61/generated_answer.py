def return_nth_smallest_ascii(s):
    distinct_chars = list(set(s[:10]))
    sorted_chars = sorted(distinct_chars)
    return sorted_chars[9] if len(sorted_chars) > 9 else None