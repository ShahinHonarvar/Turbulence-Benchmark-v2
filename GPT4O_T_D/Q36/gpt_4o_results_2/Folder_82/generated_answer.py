def filter_chars(s):
    filtered_section = [c for c in s[70:97] if not 'V' < c < 'j']
    result = s[:70] + ''.join(filtered_section) + s[97:]
    for c in set(s[70:97]) - set(filtered_section):
        result = result.replace(c, '')
    return result