def remove_repeat_chars(s):
    char_count = {}
    for i in range(86, 91):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = []
    for char in s:
        if char_count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)