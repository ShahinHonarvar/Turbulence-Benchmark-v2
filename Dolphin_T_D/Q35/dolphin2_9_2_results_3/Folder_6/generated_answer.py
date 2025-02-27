def remove_repeat_chars(s):
    repeat = set()
    for i in range(20, 93):
        if s[i] in s[i + 1:]:
            repeat.add(s[i])
    return ''.join((c for c in s if c not in repeat))