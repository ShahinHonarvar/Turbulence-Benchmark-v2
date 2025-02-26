def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    start = 11
    end = min(76, len(s))
    substring = s[start:end]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = s[:start]
    for char in s[start:]:
        if char not in repeated_chars:
            result += char
    return result