def remove_repeat_chars(s):
    part = s[56:84]
    char_count = {}
    for char in part:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)