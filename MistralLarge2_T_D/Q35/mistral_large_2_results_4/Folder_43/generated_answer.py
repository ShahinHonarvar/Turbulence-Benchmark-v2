def remove_repeat_chars(s):
    count = {}
    for i in range(10, 28):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = []
    for char in s:
        if count.get(char, 0) < 2:
            result.append(char)
    return ''.join(result)