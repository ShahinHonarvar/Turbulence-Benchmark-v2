def remove_repeat_chars(s):
    seen_chars = set()
    result = ''
    for i, char in enumerate(s):
        if 90 < i < 97:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
                if s.count(char, 90, 97) > 1:
                    result = result.replace(char, '')
                else:
                    result += char
        else:
            result += char
    return result