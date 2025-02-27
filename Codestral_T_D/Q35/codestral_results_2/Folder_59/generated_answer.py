def remove_repeat_chars(s):
    chars = {}
    result = []
    for char in s[1:10]:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    for char in s:
        if chars.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)