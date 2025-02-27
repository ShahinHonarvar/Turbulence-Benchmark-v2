def remove_repeat_chars(s):
    seen = set()
    output = ''
    for i, char in enumerate(s):
        if 32 < i < 99 and s.count(char, 32, 99) > 1:
            if char not in seen:
                seen.add(char)
                continue
        output += char
    return output