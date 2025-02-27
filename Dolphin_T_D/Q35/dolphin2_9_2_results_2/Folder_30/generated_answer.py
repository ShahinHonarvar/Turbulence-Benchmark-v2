def remove_repeat_chars(s):
    counts = {}
    for i in range(22, 25):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    to_remove = []
    for char, count in counts.items():
        if count > 1:
            to_remove.append(char)
    new_string = ''
    for i in range(len(s)):
        if s[i] not in to_remove:
            new_string += s[i]
    return new_string