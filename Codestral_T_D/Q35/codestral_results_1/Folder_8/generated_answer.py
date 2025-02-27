def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(45, 49):
        if s[i] in s[:i] + s[i + 1:49]:
            chars_to_remove.add(s[i])
    return ''.join([char for char in s if char not in chars_to_remove])