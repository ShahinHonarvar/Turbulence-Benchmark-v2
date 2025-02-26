def remove_repeat_chars(s):
    char_count = {}
    for i in range(33, 99):
        if i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
    result = []
    for char in s:
        if char in char_count and char_count[char] > 1:
            continue
        result.append(char)
    return ''.join(result)