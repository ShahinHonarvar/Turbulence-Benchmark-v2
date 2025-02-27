def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(14, min(len(s), 70)):
        if s[i] in s[14:70]:
            if s[14:70].count(s[i]) > 1:
                repeat_chars.add(s[i])
    return ''.join((ch for ch in s if ch not in repeat_chars))