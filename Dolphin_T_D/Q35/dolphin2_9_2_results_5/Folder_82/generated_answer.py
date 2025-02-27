def remove_repeat_chars(s):
    counts = {}
    for i in range(30, 200):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for char in s:
        if counts.get(char, 0) == 0:
            result += char
    return result