def remove_repeat_chars(s):
    count = {}
    for char in s[37:43]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = ''
    for char in s:
        if char[37:43] == '' or count[char] == 0:
            result += char
    return result