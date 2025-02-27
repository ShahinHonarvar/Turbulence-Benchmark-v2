def filter_chars(s):
    filtered_part = s[:44] + ''.join((c for c in s[44:68] if not 'W' < c < 'x')) + s[68:]
    return filtered_part