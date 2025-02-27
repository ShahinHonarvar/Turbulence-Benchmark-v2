def remove_repeat_chars(s):
    if len(s) <= 70:
        return s
    substring = s[71:200]
    seen = {}
    for char in substring:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    result = []
    for char in s:
        if char not in s[71:200] or seen[char] == 1:
            result.append(char)
    return ''.join(result)