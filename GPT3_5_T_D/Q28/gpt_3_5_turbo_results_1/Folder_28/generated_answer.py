def return_nth_smallest_ascii(string):
    substring = string[25:78]
    distinct_chars = list(set(substring))
    sorted_chars = sorted(distinct_chars)
    return sorted_chars[15]