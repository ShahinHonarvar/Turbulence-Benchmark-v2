def remove_repeat_chars(s):
    count = {}
    for i in range(1, 7):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = []
    for char in s:
        if count.get(char, 0) < 2:
            result.append(char)
    return ''.join(result)