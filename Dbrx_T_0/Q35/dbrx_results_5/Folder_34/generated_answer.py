def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(len(s)):
        if i >= 70 and i < 200:
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
        if i >= 70 and i < 200:
            if char_count[s[i]] == 1:
                result += s[i]
        elif s[i] not in result:
            result += s[i]
    return result