def remove_repeat_chars(s):
    counts = {}
    to_remove = set()
    for i in range(69, 99):
        if i < len(s):
            if s[i] in counts:
                to_remove.add(s[i])
            else:
                counts[s[i]] = 1
    return ''.join((char for char in s if char not in to_remove))