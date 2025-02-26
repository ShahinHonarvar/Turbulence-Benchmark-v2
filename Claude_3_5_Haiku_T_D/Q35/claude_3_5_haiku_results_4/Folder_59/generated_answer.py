def remove_repeat_chars(s):
    chars_in_range = {}
    for i in range(1, 10):
        if s[i] in chars_in_range:
            chars_in_range[s[i]] += 1
        else:
            chars_in_range[s[i]] = 1
    repeated_chars = [char for char, count in chars_in_range.items() if count > 1]
    return ''.join((char for char in s if char not in repeated_chars))