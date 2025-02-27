def remove_repeat_chars(s):
    char_count = {}
    remove_chars = set()
    for char in s[375:926]:
        if char in char_count:
            char_count[char] += 1
            remove_chars.add(char)
        else:
            char_count[char] = 1
    result = ''
    for char in s:
        if char not in remove_chars:
            result += char
    return result