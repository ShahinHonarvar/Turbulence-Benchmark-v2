def remove_repeat_chars(s: str) -> str:
    char_count = {}
    result = []
    for i in range(len(s)):
        if i >= 70 and i < 200:
            if s[i] not in char_count:
                char_count[s[i]] = 0
            char_count[s[i]] += 1
            if char_count[s[i]] == 1:
                result.append(s[i])
        else:
            result.append(s[i])
    return ''.join(result)