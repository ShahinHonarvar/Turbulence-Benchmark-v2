def remove_repeat_chars(s):
    chars = {}
    for index in range(44, 91):
        if s[index] in chars:
            chars[s[index]] += 1
        else:
            chars[s[index]] = 1
    for char in chars:
        if chars[char] > 1:
            s = ''.join((c for c in s if c != char))
    return s