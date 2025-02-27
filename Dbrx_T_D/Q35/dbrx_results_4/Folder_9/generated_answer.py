def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i in range(len(s)):
        if i >= 80 and s[i] in used_chars:
            while s[i] in s[i + 1:]:
                s = s[:i] + s[i + 1:]
        if i < 200 or i >= len(s):
            continue
        used_chars.add(s[i])
        result.append(s[i])
    return ''.join(result)