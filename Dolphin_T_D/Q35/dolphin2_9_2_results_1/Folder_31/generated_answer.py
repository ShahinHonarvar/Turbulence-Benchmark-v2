def remove_repeat_chars(s):
    count = {}
    for i in range(33, 78):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    chars_to_remove = [k for k, v in count.items() if v > 1]
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s