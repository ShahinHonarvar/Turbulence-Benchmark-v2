def remove_repeat_chars(s: str) -> str:
    char_set = set()
    non_repeat_chars = []
    for i in range(len(s)):
        if i >= 375 and i < 926 and (s[i] in char_set):
            continue
        if i >= 375 and i < 926:
            char_set.add(s[i])
        non_repeat_chars.append(s[i])
    return ''.join(non_repeat_chars)