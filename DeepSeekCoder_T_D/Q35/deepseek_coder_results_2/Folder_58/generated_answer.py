def remove_repeat_chars(s):
    char_count = {}
    for i in range(104, 802):
        char = s[i]
        if char in char_count:
            char_count[char] = True
        else:
            char_count[char] = False
    result = []
    for char in s:
        if not (104 <= s.index(char) < 802 and char_count.get(char, False)):
            result.append(char)
    return ''.join(result)