def remove_repeat_chars(s):
    chars = {}
    for i in range(34, 69):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    result = []
    for char in s:
        if char in chars and chars[char] > 1:
            continue
        else:
            result.append(char)
    return ''.join(result)