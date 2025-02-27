def remove_repeat_chars(s):
    count = {}
    result = []
    for i, char in enumerate(s):
        if 36 < i < 54:
            count[char] = count.get(char, 0) + 1
    for char in s:
        if char not in count or count[char] <= 1:
            result.append(char)
    return ''.join(result)