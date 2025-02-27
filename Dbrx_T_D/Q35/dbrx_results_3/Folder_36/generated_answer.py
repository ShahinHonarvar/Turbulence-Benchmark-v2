def remove_repeat_chars(s: str) -> str:
    char_set = set()
    non_repeat = []
    for i in range(476, 709):
        if s[i] in char_set:
            continue
        char_set.add(s[i])
        non_repeat.append(s[i])
    for i in range(709, len(s)) + list(range(476)):
        non_repeat.append(s[i])
    return ''.join(non_repeat)