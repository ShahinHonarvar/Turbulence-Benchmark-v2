def remove_repeat_chars(s):
    char_count = {}
    for char in s[:10]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = ''
    for char in s:
        if char_count.get(char, 0) <= 1:
            result += char
    return result