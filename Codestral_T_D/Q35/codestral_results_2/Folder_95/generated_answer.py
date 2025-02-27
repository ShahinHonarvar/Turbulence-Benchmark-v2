def remove_repeat_chars(s):
    char_count = {}
    result = ''
    for i in range(32, 100):
        if i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count.get(char, 0) <= 1:
            result += char
    return result