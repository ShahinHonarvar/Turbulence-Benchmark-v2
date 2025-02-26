def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(18, 88):
        if i < len(s):
            if s[i] in s[18:i] or s[i] in s[i + 1:88]:
                repeat_chars.add(s[i])
    result = ''.join((char for char in s if char not in repeat_chars))
    return result