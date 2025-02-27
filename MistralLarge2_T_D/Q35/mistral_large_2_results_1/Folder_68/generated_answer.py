def remove_repeat_chars(s):
    count = {}
    for i in range(1, 10):
        count[s[i]] = count.get(s[i], 0) + 1
    result = ''.join([ch for ch in s if count.get(ch, 0) <= 1])
    return result