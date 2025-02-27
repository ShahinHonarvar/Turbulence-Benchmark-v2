def remove_repeat_chars(s: str) -> str:
    seen_chars = {}
    start_index = 55
    end_index = 84
    for i in range(len(s)):
        if i < start_index or i >= end_index:
            continue
        if s[i] in seen_chars:
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            seen_chars[s[i]] = True
    return s