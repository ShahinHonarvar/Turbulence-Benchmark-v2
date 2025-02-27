def remove_repeat_chars(s: str) -> str:
    char_set = set()
    non_repeat_chars = []
    for i in range(len(s)):
        if i >= 103 and i < 802:
            if s[i] not in char_set:
                non_repeat_chars.append(s[i])
            char_set.add(s[i])
        else:
            non_repeat_chars.append(s[i])
    return ''.join(non_repeat_chars)