def remove_repeat_chars(s):
    substring = s[19:60]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''
    for i, char in enumerate(s):
        if i < 18 or i > 60 or char not in repeated_chars:
            result += char
    return result