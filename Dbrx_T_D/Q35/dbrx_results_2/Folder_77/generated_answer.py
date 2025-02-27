def remove_repeat_chars(s: str) -> str:
    char_set = set()
    start_index = 355
    end_index = 988
    for i in range(len(s)):
        if i < start_index or i > end_index:
            continue
        if s[i] in char_set:
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            char_set.add(s[i])
    return s