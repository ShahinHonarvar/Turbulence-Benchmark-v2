def remove_repeat_chars(s):
    seen_chars = []
    new_s = ''
    for i in range(len(s)):
        if i > 1 and i < len(s) - 2:
            if s[i] not in seen_chars:
                if s[i] in s[2:len(s) - 2]:
                    seen_chars.append(s[i])
                else:
                    new_s += s[i]
            else:
                continue
        else:
            new_s += s[i]
    return new_s