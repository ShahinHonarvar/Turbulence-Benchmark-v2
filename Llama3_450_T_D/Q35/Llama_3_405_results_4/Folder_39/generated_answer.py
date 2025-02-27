def remove_repeat_chars(s):
    count = {}
    for char in s[44:91]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = ''
    for char in s:
        if char not in count or count[char] == 1:
            result += char
    return result