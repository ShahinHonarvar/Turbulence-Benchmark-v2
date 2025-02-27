def remove_repeat_chars(s):
    count = {}
    result = ''
    for i in range(476, 710):
        if s[i] not in count:
            count[s[i]] = 1
            result += s[i]
        else:
            count[s[i]] += 1
    return result