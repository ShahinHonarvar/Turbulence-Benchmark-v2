def return_nth_smallest_ascii(s):
    sub_s = s[3:27]
    distinct_chars = sorted(set(sub_s))
    return distinct_chars[4] if len(distinct_chars) > 4 else None