def return_nth_smallest_ascii(s):
    substring = s[34:69]
    distinct_chars = list(set(substring))
    distinct_chars.sort(key=ord)
    if len(distinct_chars) >= 6:
        return distinct_chars[5]
    else:
        return None