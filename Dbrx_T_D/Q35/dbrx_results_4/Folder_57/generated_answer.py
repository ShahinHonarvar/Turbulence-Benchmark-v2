def remove_repeat_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if 25 < i < 80]
    unique_chars = list(set(filtered_chars))
    new_s = ''.join(unique_chars)
    return s[:25] + new_s + s[80:]