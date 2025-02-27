def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(len(s)):
        if i < 7 or i > 9:
            if s[i] in s[7:10] and s[7:10].count(s[i]) > 1:
                chars_to_remove.add(s[i])
    return ''.join([char for char in s if char not in chars_to_remove])