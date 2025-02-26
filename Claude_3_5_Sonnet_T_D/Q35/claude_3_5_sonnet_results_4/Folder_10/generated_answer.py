def remove_repeat_chars(s):
    if len(s) <= 37:
        return s
    target_substring = s[37:54]
    char_count = {}
    for char in target_substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeating_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''
    for char in s:
        if char not in repeating_chars:
            result += char
    return result