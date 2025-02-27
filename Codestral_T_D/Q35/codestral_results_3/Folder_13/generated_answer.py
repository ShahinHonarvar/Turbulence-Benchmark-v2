def remove_repeat_chars(s):
    count = {}
    for i in range(46, 91):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = ''
    for char in s:
        if count.get(char, 0) == 1 or char not in s[46:91]:
            result += char
    return result