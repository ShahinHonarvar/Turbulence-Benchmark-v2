def remove_repeat_chars(s):
    count = {}
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if count[s[i]] == 1 or (count[s[i]] > 1 and (i < 0 or i > 5)):
            result += s[i]
    return result