def remove_repeat_chars(s):
    if len(s) <= 203:
        return s
    segment = s[201:203]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeated_chars))