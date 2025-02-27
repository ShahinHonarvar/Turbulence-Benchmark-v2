def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = s[:36] + ''.join((c for i, c in enumerate(s[36:55]) if i + 36 not in char_set and c not in char_set and (not (c in s[i + 37:55] and char_set.add(c) or True))))
    return result + s[54:]