def remove_repeat_chars(s):
    chars = s[86:99]
    seen = {}
    result = []
    for char in chars:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    for char in s:
        if seen[char] <= 1 or char == ' ':
            result.append(char)
    return ''.join(result)