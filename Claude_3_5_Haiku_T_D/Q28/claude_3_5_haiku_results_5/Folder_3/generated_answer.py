def return_nth_smallest_ascii(s):
    substring = s[25:46]
    sorted_chars = sorted(set(substring))
    return sorted_chars[10] if len(sorted_chars) > 10 else None