def remove_repeat_chars(s):
    chars = set()
    repeat = set()
    altered = ''
    for i in range(len(s)):
        if 39 < i < 43 and s[i] in chars:
            repeat.add(s[i])
        elif s[i] not in repeat:
            chars.add(s[i])
            altered += s[i]
    return altered