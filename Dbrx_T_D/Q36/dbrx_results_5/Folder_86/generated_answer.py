def filter_chars(s):
    start_idx, end_idx = (672, 709)
    chars_to_filter = set()
    for i in range(start_idx, end_idx):
        if s[i] > 'X' and s[i] < '}':
            chars_to_filter.add(s[i])
    filtered_chars = [c for c in s if c not in chars_to_filter]
    return ''.join(filtered_chars)