def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(45, 48):
        for j in range(i + 1, 48):
            if s[i] == s[j]:
                chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result