def return_nth_smallest_ascii(s):
    if len(s) < 15:
        return None
    substring = s[:15]
    sorted_substring = sorted(substring)
    return sorted_substring[14]