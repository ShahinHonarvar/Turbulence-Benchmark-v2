def remove_repeat_chars(s):
    char_count = {}
    repeat_chars = set()
    for char in s[2:5]:
        if char in char_count:
            char_count[char] += 1
            repeat_chars.add(char)
        else:
            char_count[char] = 1
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result