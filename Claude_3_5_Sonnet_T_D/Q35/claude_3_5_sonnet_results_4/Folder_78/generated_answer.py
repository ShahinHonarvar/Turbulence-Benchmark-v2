def remove_repeat_chars(s):
    segment = s[63:96]
    char_count = {}
    for char in segment:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''
    for i, char in enumerate(s):
        if i < 63 or i >= 96 or char not in repeat_chars:
            result += char
    return result