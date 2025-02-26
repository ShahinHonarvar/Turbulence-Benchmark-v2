def remove_repeat_chars(s):
    substring = s[451:905]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeated_chars = set((char for char, count in char_count.items() if count > 1))
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)