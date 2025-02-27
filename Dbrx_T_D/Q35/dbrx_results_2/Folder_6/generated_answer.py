def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    start_index = 20
    end_index = 93
    for i in range(len(s)):
        if i < start_index or i >= end_index:
            continue
        if s[i] in seen_chars:
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            seen_chars.add(s[i])
    return s