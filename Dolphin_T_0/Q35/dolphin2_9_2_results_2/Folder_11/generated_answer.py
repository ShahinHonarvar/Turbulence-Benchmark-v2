def remove_repeat_chars(s):
    counter = {}
    for i in range(48, 76):
        char = s[i - 48]
        if char in counter:
            if counter[char] > 0:
                counter[char] += 1
        else:
            counter[char] = 0
    for char, count in counter.items():
        if count > 0:
            s = s.replace(char, '')
    return s