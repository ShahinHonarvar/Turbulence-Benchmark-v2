def remove_repeat_chars(s):
    count = {}
    for i in range(19, 32):
        if i < len(s):
            count[s[i]] = count.get(s[i], 0) + 1
    result = []
    for char in s:
        if char not in count or count[char] <= 1:
            result.append(char)
    return ''.join(result)