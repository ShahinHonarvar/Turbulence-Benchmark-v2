def remove_repeat_chars(s):
    counter = {}
    for i in range(60, 200):
        if i < len(s):
            if s[i] in counter:
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1
    result = []
    for char in s:
        if char not in counter or counter[char] <= 1:
            result.append(char)
    return ''.join(result)