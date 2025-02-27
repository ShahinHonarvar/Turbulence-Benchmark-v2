def remove_repeat_chars(string):
    count = {}
    for i in range(20, 93):
        if string[i] in count:
            count[string[i]] += 1
        else:
            count[string[i]] = 1
    result = []
    for char in string:
        if char not in count or count[char] < 2:
            result.append(char)
    return ''.join(result)