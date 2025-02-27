def return_nth_smallest_ascii(s):
    distinct_chars = sorted(set(s[1:67]))
    return distinct_chars[7]