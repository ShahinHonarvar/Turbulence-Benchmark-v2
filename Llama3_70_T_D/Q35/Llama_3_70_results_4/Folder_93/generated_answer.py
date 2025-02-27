def remove_repeat_chars(s):
    char_count = {}
    for i in range(57, 85):
        if i < len(s) and s[i] in char_count:
            char_count[s[i]] += 1
        elif i < len(s):
            char_count[s[i]] = 1
    result = []
    for char in s:
        if char not in char_count or char_count[char] == 1:
            result.append(char)
    return ''.join(result)