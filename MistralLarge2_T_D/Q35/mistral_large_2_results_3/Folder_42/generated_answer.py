def remove_repeat_chars(s):
    count = {}
    for i in range(18, 60):
        if i < len(s) and s[i] in count:
            count[s[i]] += 1
        elif i < len(s):
            count[s[i]] = 1
    result = []
    for char in s:
        if char not in count or count[char] == 1:
            result.append(char)
    return ''.join(result)