def filter_chars(s):
    chars_to_filter = [s[i] for i in range(54, 92) if s[i] > 'J' and s[i] < 'X']
    return ''.join([ch for ch in s if ch not in chars_to_filter])