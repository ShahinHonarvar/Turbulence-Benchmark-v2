def remove_repeat_chars(s):
    seen = set()
    to_remove = set()
    for i in range(462, 995):
        if s[i] in seen:
            to_remove.add(s[i])
        else:
            seen.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)