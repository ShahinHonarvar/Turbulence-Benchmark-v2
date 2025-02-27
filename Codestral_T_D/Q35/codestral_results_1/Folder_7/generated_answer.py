def remove_repeat_chars(s):
    chars = {}
    for i in range(376, 926):
        char = s[i]
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    result = ''
    for char in s:
        if chars[char] <= 1 or char not in s[376:926]:
            result += char
    return result