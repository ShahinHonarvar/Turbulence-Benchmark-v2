def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('g'), ord('o'))}
    filtered_string = ''.join((c for c in s if c not in chars_to_remove or not 23 < s.index(c) < 83))
    return filtered_string