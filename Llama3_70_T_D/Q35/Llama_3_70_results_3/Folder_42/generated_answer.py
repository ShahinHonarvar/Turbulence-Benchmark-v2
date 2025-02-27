def remove_repeat_chars(s):
    count = {}
    for i in range(18, 60):
        if i < len(s) and s[i] in count:
            count[s[i]] += 1
        elif i < len(s) and s[i] not in count:
            count[s[i]] = 1
    remove = [key for key, value in count.items() if value > 1]
    return ''.join([c for c in s if c not in remove])