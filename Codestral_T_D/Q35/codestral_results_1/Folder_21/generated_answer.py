def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(463, 995):
        if s[i] in s[i + 1:995]:
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))