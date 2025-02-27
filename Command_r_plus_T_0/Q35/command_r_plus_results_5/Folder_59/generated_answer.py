def remove_repeat_chars(s):
    unique_chars = set(s[:10])
    result = ''.join((c for c in s if c in unique_chars))
    return result