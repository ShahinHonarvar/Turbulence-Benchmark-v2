def remove_repeat_chars(s):
    count = {}
    for i in range(69, 97):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = [k for k, v in count.items() if v > 1]
    result = ''
    for i in range(len(s)):
        if s[i] not in repeat_chars:
            result += s[i]
    return result