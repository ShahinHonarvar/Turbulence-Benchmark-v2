def filter_chars(s):
    chars_to_remove = [s[i] for i in range(259, 503) if ',' <= s[i] <= '3']
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result