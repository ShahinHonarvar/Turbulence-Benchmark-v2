def remove_repeat_chars(s):
    char_count = {}
    for char in s[36:52]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = set()
    for char, count in char_count.items():
        if count > 1:
            repeat_chars.add(char)
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result