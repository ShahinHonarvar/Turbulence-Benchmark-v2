def remove_repeat_chars(s):
    if len(s) <= 45:
        return s
    substring = s[46:48]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) <= 45 or s.index(char) >= 48))
    return result