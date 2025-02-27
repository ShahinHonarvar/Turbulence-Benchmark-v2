def remove_repeat_chars(s):
    char_counts = {}
    for i in range(40, 200):
        if s[i] != ' ':
            if s[i] in char_counts:
                char_counts[s[i]] += 1
            else:
                char_counts[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if i < 40 or i >= 200:
            result += s[i]
        elif s[i] not in char_counts or char_counts[s[i]] == 1:
            result += s[i]
    return result