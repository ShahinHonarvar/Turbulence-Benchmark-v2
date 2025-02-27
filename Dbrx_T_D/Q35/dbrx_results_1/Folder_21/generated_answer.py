def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count and 462 <= i < 995:
            char_count[s[i]] += 1
            if char_count[s[i]] > 1:
                s = s[:i] + s[i + 1:]
                i -= 1
        elif 462 <= i < 995:
            char_count[s[i]] = 1
    return s