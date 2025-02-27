def remove_repeat_chars(s):
    if len(s) <= 39:
        return s
    counter = {}
    for i in range(39, min(len(s) - 1, 81)):
        if s[i] in counter:
            counter[s[i]] += 1
        else:
            counter[s[i]] = 1
    chars_to_remove = {char for char, count in counter.items() if count > 1}
    result = []
    for i in range(len(s)):
        if i <= 38 or i >= 82 or s[i] not in chars_to_remove:
            result.append(s[i])
    return ''.join(result)