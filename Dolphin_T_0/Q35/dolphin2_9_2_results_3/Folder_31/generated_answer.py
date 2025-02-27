def remove_repeat_chars(s):
    chars = [0] * 128
    for i in range(33, 78):
        chars[ord(s[i])] += 1
    new_str = ''
    for i in range(len(s)):
        if s[i] not in s[33:78] or chars[ord(s[i])] == 1:
            new_str += s[i]
    return new_str