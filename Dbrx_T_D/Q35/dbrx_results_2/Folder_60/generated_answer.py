def remove_repeat_chars(s):
    found_chars = set()
    result = []
    i = 0
    while i < len(s):
        if 38 <= i < 52:
            if s[i] in found_chars:
                i += 1
                continue
            found_chars.add(s[i])
        result.append(s[i])
        i += 1
    return ''.join(result)