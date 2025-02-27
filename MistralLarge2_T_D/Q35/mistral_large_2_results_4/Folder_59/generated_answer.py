def remove_repeat_chars(s):
    count = {}
    for char in s[1:10]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = []
    for char in s:
        if char not in count or count[char] == 1:
            result.append(char)
    return ''.join(result)