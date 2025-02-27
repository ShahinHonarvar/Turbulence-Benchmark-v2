def remove_repeat_chars(s):
    char_count = {}
    for char in s[1:8]:
        char_count[char] = char_count.get(char, 0) + 1
    result = []
    for char in s:
        if char not in char_count or char_count[char] < 2:
            result.append(char)
    return ''.join(result)