def remove_repeat_chars(s):
    char_count = {}
    for i in range(25, 80):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if i < 25 or i >= 80 or s[i] not in char_count or (char_count[s[i]] == 1):
            result += s[i]
    return result