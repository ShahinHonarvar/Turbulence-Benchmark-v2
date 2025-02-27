def remove_repeat_chars(s):
    seen = {}
    result = []
    for i in range(len(s)):
        if i < 10:
            if s[i] in seen:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1
    for char in s:
        if char in seen and seen[char] <= 1:
            result.append(char)
        elif char not in seen:
            result.append(char)
    return ''.join(result)