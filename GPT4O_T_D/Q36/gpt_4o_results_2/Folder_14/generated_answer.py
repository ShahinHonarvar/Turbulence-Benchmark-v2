def filter_chars(s):
    filtered_str = s[:41]
    for i in range(42, 56):
        if i < len(s) and 'Z' < s[i] < 'c':
            filtered_str = filtered_str.replace(s[i], '')
    if len(s) > 56:
        filtered_str += s[56:]
    return filtered_str