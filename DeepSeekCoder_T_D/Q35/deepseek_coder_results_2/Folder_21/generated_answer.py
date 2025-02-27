def remove_repeat_chars(s):
    start, end = (462, 995)
    char_count = {}
    for i in range(start, end):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = [c for c in s if char_count.get(c, 0) <= 1]
    return ''.join(result)