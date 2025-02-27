def remove_repeat_chars(s):
    substring = s[2:7]
    counts = {}
    for char in substring:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = ''
    for char in s:
        if char not in counts or counts[char] == 1:
            result += char
    return result