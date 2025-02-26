def remove_repeat_chars(s):
    if len(s) <= 926:
        return s
    substring = s[376:926]
    char_counts = {}
    repeated_chars = set()
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
        if char_counts[char] > 1:
            repeated_chars.add(char)
    return ''.join((char for char in s if char not in repeated_chars))