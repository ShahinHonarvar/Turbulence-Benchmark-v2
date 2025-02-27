def remove_repeat_chars(s):
    count = {}
    for i in range(34, 69):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for i in s:
        if count.get(i, 0) == 0:
            result += i
    return result