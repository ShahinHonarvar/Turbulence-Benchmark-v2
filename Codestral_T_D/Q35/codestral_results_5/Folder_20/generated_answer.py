def remove_repeat_chars(s):
    count = {}
    for i in range(27, 96):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = ''
    for char in s:
        if count.get(char, 0) <= 1:
            result += char
    return result