def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(len(s)):
        if i >= 57 and i < 85:
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
        elif s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if i >= 57 and i < 85:
            if char_count[s[i]] == 1:
                result += s[i]
        else:
            result += s[i]
    return result