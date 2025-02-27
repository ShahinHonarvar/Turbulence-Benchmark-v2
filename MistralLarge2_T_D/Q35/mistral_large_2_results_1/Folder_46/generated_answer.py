def remove_repeat_chars(s):
    counter = {}
    for i in range(10, 80):
        if i < len(s):
            char = s[i]
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    result = []
    for char in s:
        if counter.get(char, 0) <= 1:
            result.append(char)
    return ''.join(result)