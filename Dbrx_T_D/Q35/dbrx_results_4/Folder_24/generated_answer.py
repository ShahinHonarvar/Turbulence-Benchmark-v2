def remove_repeat_chars(s):
    seen = set()
    output = []
    for i in range(len(s)):
        if i >= 13 and i < 91:
            if s[i] in seen:
                continue
            seen.add(s[i])
        output.append(s[i])
    return ''.join(output)