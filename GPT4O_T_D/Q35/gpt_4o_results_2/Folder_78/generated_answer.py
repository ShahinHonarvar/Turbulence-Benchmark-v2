def remove_repeat_chars(s):
    sub_str = s[63:96]
    char_counts = {}
    for char in sub_str:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result