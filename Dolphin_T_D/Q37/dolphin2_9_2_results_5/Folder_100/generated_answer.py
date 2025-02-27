def filter_chars(s):
    chars_to_filter = [s[i] for i in range(88, 91) if s[i] >= 'J' and s[i] <= 'Q']
    filtered_s = ''.join([c for c in s if c not in chars_to_filter])
    return filtered_s