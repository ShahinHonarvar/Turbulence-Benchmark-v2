def remove_repeat_chars(s):
    count = {}
    for i in range(462, 995):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    return ''.join((c for c in s if count.get(c, 0) <= 1))