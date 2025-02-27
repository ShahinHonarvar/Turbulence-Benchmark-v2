def remove_repeat_chars(s):
    seen = {}
    result = []
    for i, char in enumerate(s):
        if 0 <= i < 9:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
    for char in s:
        if 0 <= s.index(char) < 9 and seen.get(char, 0) > 1:
            continue
        result.append(char)
    return ''.join(result)