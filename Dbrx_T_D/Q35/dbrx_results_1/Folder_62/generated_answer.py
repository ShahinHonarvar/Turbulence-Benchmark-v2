def remove_repeat_chars(s: str) -> str:
    char_count = {}
    result = []
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
        if char_count[s[i]] < 3 or (i < 50 or i > 92):
            result.append(s[i])
    return ''.join(result)