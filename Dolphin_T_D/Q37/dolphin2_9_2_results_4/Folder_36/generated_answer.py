def filter_chars(s):
    chars_to_remove = {char for idx, char in enumerate(s) if 259 <= idx <= 502 and ',' <= char <= '3'}
    new_s = [char for char in s if char not in chars_to_remove]
    return ''.join(new_s)