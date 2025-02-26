def remove_repeat_chars(s):
    count = {}
    result = []
    for i, char in enumerate(s):
        if i == 0 or i == 9:
            result.append(char)
        elif 0 < i < 9:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        else:
            result.append(char)
    for i, char in enumerate(s):
        if 0 < i < 9:
            if count[char] == 1:
                result.insert(i, char)
    return ''.join(result)