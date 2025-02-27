def remove_repeat_chars(s):
    chars = {}
    for i in range(86, 99):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    new_s = ''
    for char in s:
        if char in chars and chars[char] > 1:
            continue
        new_s += char
    return new_s