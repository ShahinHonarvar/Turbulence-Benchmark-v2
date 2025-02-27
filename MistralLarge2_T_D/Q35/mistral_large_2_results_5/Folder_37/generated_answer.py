def remove_repeat_chars(s):
    count = {}
    for i in range(2, 7):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = [c for c in s if count.get(c, 0) <= 1]
    return ''.join(result)