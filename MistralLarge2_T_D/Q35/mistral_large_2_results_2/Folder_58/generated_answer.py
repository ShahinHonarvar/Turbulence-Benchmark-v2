def remove_repeat_chars(s):
    count = {}
    for i in range(103, 802):
        if i < len(s):
            char = s[i]
            count[char] = count.get(char, 0) + 1
    result = []
    for char in s:
        if count.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)