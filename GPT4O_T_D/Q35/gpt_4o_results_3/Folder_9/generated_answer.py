def remove_repeat_chars(s):
    substring = s[81:200]
    char_count = {}
    for char in substring:
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