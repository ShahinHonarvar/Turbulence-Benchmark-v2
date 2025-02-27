def remove_repeat_chars(s: str) -> str:
    for i in range(len(s)):
        if 7 <= i < 9:
            char_set = set(s[i])
            char_list = list(s)
            for char in char_set:
                while True:
                    try:
                        char_list.remove(char)
                    except ValueError:
                        break
            s = ''.join(char_list)
    return s