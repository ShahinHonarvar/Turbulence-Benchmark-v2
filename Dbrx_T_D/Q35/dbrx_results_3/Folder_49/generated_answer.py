def remove_repeat_chars(s: str) -> str:
    char_indices = {}
    altered_s = ''
    for i in range(len(s)):
        if s[i] not in char_indices:
            char_indices[s[i]] = i
        elif char_indices[s[i]] > 90 and char_indices[s[i]] < 200:
            continue
        else:
            altered_s += s[i]
            char_indices[s[i]] = i
    return altered_s