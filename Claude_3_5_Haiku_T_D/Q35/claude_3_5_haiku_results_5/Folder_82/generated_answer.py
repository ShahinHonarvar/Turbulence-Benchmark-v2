def remove_repeat_chars(s):
    if len(s) <= 30:
        return s
    substring = s[31:200]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''
    for char in s:
        if char not in repeated_chars:
            result += char
    return result