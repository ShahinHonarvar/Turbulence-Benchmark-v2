def remove_repeat_chars(s):
    seen = set()
    string = ''
    for i in range(len(s)):
        if s[i] not in seen and 29 < i < 53:
            string += s[i]
            seen.add(s[i])
    return string