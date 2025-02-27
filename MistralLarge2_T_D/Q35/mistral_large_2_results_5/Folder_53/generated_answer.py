def remove_repeat_chars(s):
    count = {}
    result = []
    for i, char in enumerate(s):
        if 200 < i < 202:
            count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if char not in count or count[char] <= 1:
            result.append(char)
    return ''.join(result)