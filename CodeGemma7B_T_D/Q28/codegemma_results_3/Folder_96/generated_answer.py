def return_nth_smallest_ascii(distinct_chars):
    sorted_chars = sorted(distinct_chars[0:18], key=ord)
    return sorted_chars[17]