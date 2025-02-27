def remove_repeat_chars(s):
    chars = {}
    for i in range(56, 84):
        char = s[i]
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return ''.join((c for c in s if chars.get(c, 0) == 1))