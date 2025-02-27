def remove_repeat_chars(s):
    s = list(s)
    count = {}
    repeat_chars = set()
    for i in range(38, 81):
        if s[i] in count:
            count[s[i]] += 1
            repeat_chars.add(s[i])
        else:
            count[s[i]] = 1
    for char in repeat_chars:
        repeat_indexes = [i for i, c in enumerate(s) if c == char]
        for index in sorted(repeat_indexes, reverse=True):
            del s[index]
    return ''.join(s)