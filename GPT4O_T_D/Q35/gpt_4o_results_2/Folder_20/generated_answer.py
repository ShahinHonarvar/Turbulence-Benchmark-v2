def remove_repeat_chars(s):
    count = {}
    for i in range(28, min(96, len(s))):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = []
    for i, char in enumerate(s):
        if count.get(char, 0) <= 1 or i <= 27 or i >= 96:
            result.append(char)
    return ''.join(result)