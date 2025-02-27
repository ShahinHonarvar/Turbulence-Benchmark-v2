def remove_repeat_chars(s):
    counts = [0] * 128
    for i in range(13, 91):
        counts[ord(s[i])] += 1
    result = ''
    for char in s:
        if counts[ord(char)] <= 1:
            result += char
    return result