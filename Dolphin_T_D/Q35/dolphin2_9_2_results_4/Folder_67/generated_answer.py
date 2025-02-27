def remove_repeat_chars(s):
    counts = {}
    for i in range(44, 67):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    to_remove = [char for char, count in counts.items() if count > 1]
    new_s = ''
    for i in range(len(s)):
        if s[i] not in to_remove:
            new_s += s[i]
    return new_s