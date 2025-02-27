def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count and 450 < i < 905:
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            if i not in char_count:
                char_count[s[i]] = 0
            char_count[s[i]] += 1
    return s