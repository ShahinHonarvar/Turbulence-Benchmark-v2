def remove_repeat_chars(s):
    char_count = {}
    for i in range(44, 91):
        if i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
    result = ''
    for char in s:
        if char not in char_count or char_count[char] == 1:
            result += char
    return result