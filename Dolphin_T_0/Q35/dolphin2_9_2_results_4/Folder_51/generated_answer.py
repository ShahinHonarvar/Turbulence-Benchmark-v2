def remove_repeat_chars(s):
    counted_chars = [s[i] for i in range(6, 10) if s[i] not in s[:6]]
    modified_string = ''.join([c for c in s if c not in counted_chars])
    return modified_string