def remove_repeat_chars(s):
    seen = {}
    for i in range(42, 87):
        if s[i] in seen:
            seen[s[i]] += 1
        else:
            seen[s[i]] = 1
    result = []
    for char in s:
        if char not in seen or seen[char] == 1:
            result.append(char)
        else:
            seen[char] -= 1
    return ''.join(result)