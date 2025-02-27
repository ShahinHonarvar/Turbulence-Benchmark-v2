def remove_repeat_chars(s: str) -> str:
    char_set = set()
    char_list = []
    for i in range(len(s)):
        if i >= 20 and i < 200 and (s[i] in char_set):
            continue
        char_set.add(s[i])
        char_list.append(s[i])
    return ''.join(char_list)