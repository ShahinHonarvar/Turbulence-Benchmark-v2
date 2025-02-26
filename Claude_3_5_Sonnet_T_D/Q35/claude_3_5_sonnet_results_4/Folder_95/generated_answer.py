def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    start = 33
    end = min(99, len(s))
    substr = s[start:end]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeats = set((char for char, count in char_count.items() if count > 1))
    result = s[:start]
    for char in s[start:]:
        if char not in repeats:
            result += char
    return result