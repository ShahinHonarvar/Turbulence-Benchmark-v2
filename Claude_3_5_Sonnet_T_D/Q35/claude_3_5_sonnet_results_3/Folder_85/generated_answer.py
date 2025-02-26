def remove_repeat_chars(s):
    count = {}
    result = s[0]
    for i in range(1, len(s)):
        if i > 1 and i < 8:
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        if s[i] not in count or count[s[i]] == 1:
            result += s[i]
    return result