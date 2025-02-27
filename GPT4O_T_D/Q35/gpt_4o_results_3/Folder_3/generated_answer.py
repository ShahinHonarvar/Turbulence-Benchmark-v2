def remove_repeat_chars(s):
    target_part = s[57:88]
    char_count = {}
    for char in target_part:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    remove_chars = {char for char, count in char_count.items() if count > 1}
    result = []
    for char in s:
        if char not in remove_chars:
            result.append(char)
    return ''.join(result)