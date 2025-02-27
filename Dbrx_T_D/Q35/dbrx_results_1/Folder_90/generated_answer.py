def remove_repeat_chars(s):
    chars = s[306:807]
    for char in set(chars):
        if chars.count(char) > 1:
            s = s.replace(char, '', chars.count(char))
    return s