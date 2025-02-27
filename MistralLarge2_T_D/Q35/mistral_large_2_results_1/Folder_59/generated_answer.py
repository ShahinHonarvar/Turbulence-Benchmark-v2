def remove_repeat_chars(s):
    count = {}
    for i in range(1, 10):
        if s[i] not in count:
            count[s[i]] = 1
        else:
            count[s[i]] += 1
    result = [s[i] for i in range(len(s)) if count.get(s[i], 0) <= 1]
    return ''.join(result)