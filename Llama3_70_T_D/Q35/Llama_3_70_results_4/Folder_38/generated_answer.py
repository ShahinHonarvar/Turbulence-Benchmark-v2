def remove_repeat_chars(s):
    count = {}
    for char in s[36:85]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = []
    for char in s:
        if count.get(char, 1) == 1:
            result.append(char)
    return ''.join(result)