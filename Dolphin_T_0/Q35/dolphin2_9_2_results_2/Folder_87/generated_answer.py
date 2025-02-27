def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 43):
        if s[i] in counts and counts[s[i]] < 2:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    result = ''
    for char in s:
        if char not in counts or counts[char] > 1:
            result += char
    return result