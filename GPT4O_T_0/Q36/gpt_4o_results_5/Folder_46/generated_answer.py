def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('<') + 1, ord('C'))}
    filtered_string = s[:19] + ''.join((c for c in s[20:69] if c not in chars_to_remove)) + s[69:]
    return filtered_string