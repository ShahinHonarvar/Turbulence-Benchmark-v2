def remove_repeat_chars(s):
    unique_chars = set()
    to_remove = set()
    for i in range(73, 84):
        if s[i] in unique_chars:
            to_remove.add(s[i])
        else:
            unique_chars.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result