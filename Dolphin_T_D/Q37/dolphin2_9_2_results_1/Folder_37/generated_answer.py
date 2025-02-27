def filter_chars(s):
    chars_to_filter = [s[i] for i in range(17, 64) if 'O' <= s[i] <= '^']
    new_string = [char for char in s if char not in chars_to_filter]
    return ''.join(new_string)