def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(330, 543):
        if s.count(s[i]) > 1:
            repeated_chars.add(s[i])
    return ''.join([c for c in s if c not in repeated_chars])