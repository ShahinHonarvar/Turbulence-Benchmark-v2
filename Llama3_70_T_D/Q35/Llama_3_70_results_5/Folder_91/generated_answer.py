def remove_repeat_chars(s):
    seen = set()
    repeat_chars = set()
    for char in s[:7]:
        if char in seen:
            repeat_chars.add(char)
        seen.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)