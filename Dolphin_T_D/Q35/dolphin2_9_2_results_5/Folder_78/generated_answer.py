def remove_repeat_chars(s):
    counter = {}
    for c in s[62:96]:
        if c in counter and counter[c] < 1:
            counter[c] += 1
        else:
            counter[c] = 1
    result = ''
    for c in s:
        if c in counter and counter[c] < 1:
            result += c
    return result