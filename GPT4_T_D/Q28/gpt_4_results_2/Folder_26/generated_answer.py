def return_nth_smallest_ascii(distinct_string):
    substring = distinct_string[1:37]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[14]