def remove_repeat_chars(s):
    counter = {}
    for i in range(330, 543):
        if i < len(s):
            if s[i] in counter:
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1
    result = []
    for char in s:
        if counter.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)