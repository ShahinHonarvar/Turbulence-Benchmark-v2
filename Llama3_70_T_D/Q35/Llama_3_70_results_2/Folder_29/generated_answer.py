def remove_repeat_chars(s):
    count = {}
    for i in range(70, 98):
        if i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    to_remove = set()
    for k, v in count.items():
        if v > 1:
            to_remove.add(k)
    result = ''
    for c in s:
        if c not in to_remove:
            result += c
    return result