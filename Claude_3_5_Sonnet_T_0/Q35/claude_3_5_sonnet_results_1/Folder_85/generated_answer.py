def remove_repeat_chars(s):
    count = {}
    for i in range(1, 8):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    result = s[0]
    for i in range(1, len(s)):
        if i < 8:
            if count[s[i]] <= 1:
                result += s[i]
        elif s[i] not in count or count[s[i]] <= 1:
            result += s[i]
    return result