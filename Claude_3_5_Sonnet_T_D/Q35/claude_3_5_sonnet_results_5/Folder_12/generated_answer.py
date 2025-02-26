def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    start, end = (16, 87)
    mid_section = s[start:end]
    char_count = {}
    for char in mid_section:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = s[:start]
    for char in s[start:]:
        if char not in repeated_chars:
            result += char
    return result