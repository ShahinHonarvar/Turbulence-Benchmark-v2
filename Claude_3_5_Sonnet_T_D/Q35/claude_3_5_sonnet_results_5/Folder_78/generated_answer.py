def remove_repeat_chars(s):
    target_segment = s[63:96]
    char_counts = {}
    for char in target_segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''
    for char in s:
        if char not in repeated_chars:
            result += char
    return result