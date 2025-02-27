def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(356, 988):
        if s[i] in s[i + 1:988]:
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))