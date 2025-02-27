def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(20, 35):
        for j in range(i + 1, 35):
            if s[i] == s[j]:
                chars_to_remove.add(s[i])
    new_string = ''
    for char in s:
        if char not in chars_to_remove:
            new_string += char
    return new_string