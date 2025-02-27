def remove_repeat_chars(s):
    chars = {}
    for i in range(38, 81):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    return ''.join([char for char in s if chars.get(char, 0) <= 1])