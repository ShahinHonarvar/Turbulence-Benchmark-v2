def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if 86 < i < 99:
            if char in s[87:99] and char not in seen_chars:
                seen_chars.add(char)
            elif char in seen_chars:
                continue
        result.append(char)
    return ''.join(result)