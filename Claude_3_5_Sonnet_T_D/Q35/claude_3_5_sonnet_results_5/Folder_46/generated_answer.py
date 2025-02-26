def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    start = 11
    end = min(79, len(s))
    middle = s[start:end]
    char_counts = {}
    for char in middle:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_counts.items() if count > 1))
    result = s[:start]
    for char in s[start:]:
        if char not in chars_to_remove:
            result += char
    return result