def remove_repeat_chars(s):
    if len(s) <= 47:
        return s
    start = 47
    end = min(91, len(s))
    chars_to_remove = set()
    for i in range(start, end):
        if s[i] in s[start:i] or s[i] in s[i + 1:end]:
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))