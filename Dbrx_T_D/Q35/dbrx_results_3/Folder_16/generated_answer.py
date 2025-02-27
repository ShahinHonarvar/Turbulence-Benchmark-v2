def remove_repeat_chars(s: str) -> str:
    char_freq = {}
    for i in range(len(s)):
        if i >= 90 and i < 97:
            if s[i] in char_freq:
                char_freq[s[i]] += 1
            else:
                char_freq[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if i < 90 or i >= 97 or char_freq[s[i]] == 1:
            result += s[i]
    return result