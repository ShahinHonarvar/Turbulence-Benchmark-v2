def return_nth_smallest_ascii(s):
    section = s[13:36]
    sorted_section = sorted(section)
    return sorted_section[17] if len(sorted_section) >= 18 else None