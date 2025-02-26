def remove_repeat_chars(s):
    chars_count = {}
    for i in range(33, 99):
        if 0 <= i < len(s):
            chars_count[s[i]] = chars_count.get(s[i], 0) + 1
    repeat_chars = set((char for char, count in chars_count.items() if count > 1))
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)