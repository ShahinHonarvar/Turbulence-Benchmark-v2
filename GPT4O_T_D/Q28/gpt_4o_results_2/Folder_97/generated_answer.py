def return_nth_smallest_ascii(s):
    sub_string = s[15:22]
    sorted_substring = sorted(sub_string)
    return sorted_substring[5] if len(sorted_substring) >= 6 else None