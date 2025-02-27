def remove_repeat_chars(s: str) -> str:
    char_set = set()
    char_list = []
    for char in s[1:10]:
        if char not in char_set:
            char_set.add(char)
            char_list.append(char)
    return ''.join(char_list) + s[:1] + s[10:]