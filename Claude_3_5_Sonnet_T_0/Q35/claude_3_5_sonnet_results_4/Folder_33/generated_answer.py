def remove_repeat_chars(s):
    if len(s) <= 126:
        return s
    start = 126
    end = min(825, len(s))
    substring = s[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    chars_to_remove = set((char for char, count in char_count.items() if count > 1))
    result = s[:start]
    for char in s[start:]:
        if char not in chars_to_remove:
            result += char
    return result