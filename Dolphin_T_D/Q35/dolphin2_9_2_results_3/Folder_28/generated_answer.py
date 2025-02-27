def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(86, 99):
        for j in range(i + 1, 99):
            if s[i] == s[j]:
                repeat_chars.add(s[i])
    new_s = ''
    for char in s:
        if char not in repeat_chars:
            new_s += char
    return new_s