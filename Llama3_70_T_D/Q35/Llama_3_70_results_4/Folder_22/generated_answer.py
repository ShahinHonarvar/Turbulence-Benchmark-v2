def remove_repeat_chars(s):
    repeat_chars = set()
    for char in s[50:200]:
        if s[50:200].count(char) > 1:
            repeat_chars.add(char)
    return ''.join([char for char in s if char not in repeat_chars])