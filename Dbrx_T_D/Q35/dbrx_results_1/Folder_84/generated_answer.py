def remove_repeat_chars(s: str) -> str:
    char_count = {}
    result = []
    for i in range(32, 45):
        char_count[s[i]] = 0
    for char in s[32:45]:
        char_count[char] += 1
    for i in range(len(s)):
        if i < 32 or i >= 45 or char_count[s[i]] == 1:
            result.append(s[i])
    return ''.join(result)