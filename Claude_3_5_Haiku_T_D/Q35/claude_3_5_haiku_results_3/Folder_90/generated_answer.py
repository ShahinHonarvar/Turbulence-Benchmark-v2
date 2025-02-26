def remove_repeat_chars(s):
    if len(s) <= 807:
        return s
    substring = s[307:807]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 307 or s.index(char) >= 807))