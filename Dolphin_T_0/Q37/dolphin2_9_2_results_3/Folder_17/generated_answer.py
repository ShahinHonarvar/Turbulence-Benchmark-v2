def filter_chars(s):
    chars_to_remove = [s[i] for i in range(27, 30) if ';' <= s[i] <= 'b']
    filtered_s = ''.join([ch for ch in s if ch not in chars_to_remove])
    return filtered_s