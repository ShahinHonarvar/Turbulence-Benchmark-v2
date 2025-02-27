def remove_repeat_chars(s):
    char_count = {}
    for char in s[355:988]:
        char_count[char] = char_count.get(char, 0) + 1
    result = ''
    for char in s:
        if char_count.get(char, 0) <= 1:
            result += char
    return result