def remove_repeat_chars(s):
    counts = {}
    for i in range(8):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
    result = ''
    for char in s:
        if counts[char] == 1:
            result += char
    return result