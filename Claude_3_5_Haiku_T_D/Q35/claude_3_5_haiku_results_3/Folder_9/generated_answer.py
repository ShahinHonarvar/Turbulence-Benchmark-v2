def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    substring = s[81:200]
    char_counts = {}
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_counts.items() if count > 1))
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result