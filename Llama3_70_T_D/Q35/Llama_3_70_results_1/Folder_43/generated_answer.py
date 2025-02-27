def remove_repeat_chars(s):
    count = {}
    for i in range(len(s)):
        if i > 10 and i < 28:
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
    result = ''
    for char in s:
        keep = True
        for key in count:
            if char == key and count[key] > 1:
                keep = False
                break
        if keep:
            result += char
    return result