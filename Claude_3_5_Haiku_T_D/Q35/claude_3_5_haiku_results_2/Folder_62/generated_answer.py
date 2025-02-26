def remove_repeat_chars(s):
    if len(s) <= 92:
        return s
    substr = s[51:92]
    char_count = {}
    for char in substr:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 51 or s.index(char) >= 92))
    return result