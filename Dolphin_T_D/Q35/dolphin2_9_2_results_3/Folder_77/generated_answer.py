def remove_repeat_chars(s):
    count = {}
    for i in range(355, 988):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    repeat_chars = [key for key, value in count.items() if value > 1]
    result = ''
    for i in range(len(s)):
        if i < 355 or i >= 988 or s[i] not in repeat_chars:
            result += s[i]
    return result