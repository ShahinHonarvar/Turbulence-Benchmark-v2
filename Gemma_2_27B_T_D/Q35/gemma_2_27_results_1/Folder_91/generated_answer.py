def remove_repeat_chars(s):
    seen = {}
    for i in range(7):
        if s[i] in seen:
            seen[s[i]] += 1
        else:
            seen[s[i]] = 1
    result = []
    for char in s:
        if char in seen and seen[char] == 1:
            result.append(char)
    return ''.join(result)