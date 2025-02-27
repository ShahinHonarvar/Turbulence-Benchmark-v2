def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(44, 67, 1):
        for j in range(i + 1, 67, 1):
            if s[i] == s[j]:
                chars_to_remove.add(s[i])
    new_string = ''
    for i in s:
        if not i in chars_to_remove:
            new_string += i
    return new_string