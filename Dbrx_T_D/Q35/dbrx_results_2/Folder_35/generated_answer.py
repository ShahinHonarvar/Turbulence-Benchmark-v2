def remove_repeat_chars(s):
    char_list = []
    seen_chars = set()
    for i in range(len(s)):
        if 77 < i < 84 and s[i] not in seen_chars:
            char_list.append(s[i])
            seen_chars.add(s[i])
        elif i not in range(77, 85):
            char_list.append(s[i])
    return ''.join(char_list)