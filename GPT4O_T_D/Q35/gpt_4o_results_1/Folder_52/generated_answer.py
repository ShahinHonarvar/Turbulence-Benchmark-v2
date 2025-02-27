def remove_repeat_chars(s):
    counter = {}
    for i in range(39, 81):
        if i < len(s):
            char = s[i]
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    result = []
    for i, char in enumerate(s):
        if 39 <= i < 81 and counter.get(char, 0) > 1:
            continue
        result.append(char)
    return ''.join(result)