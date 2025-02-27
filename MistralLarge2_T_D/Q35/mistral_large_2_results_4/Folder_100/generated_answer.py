def remove_repeat_chars(s):
    counts = {}
    for i in range(44, 78):
        counts[s[i]] = counts.get(s[i], 0) + 1
    return ''.join([char for char in s if counts.get(char, 0) <= 1])