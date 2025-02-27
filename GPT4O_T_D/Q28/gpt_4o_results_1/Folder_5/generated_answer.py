def return_nth_smallest_ascii(distinct_chars):
    relevant_chars = distinct_chars[5:90]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[12] if len(sorted_chars) >= 13 else None