def remove_repeat_chars(s):
    count = {}
    for i in range(306, 807):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    result = [ch for ch in s if count.get(ch, 0) <= 1]
    return ''.join(result)