def return_nth_smallest_ascii(s):
    filtered_chars = s[50:90]
    distinct_chars = list(set(filtered_chars))
    distinct_chars.sort(key=lambda x: ord(x))
    return distinct_chars[13]