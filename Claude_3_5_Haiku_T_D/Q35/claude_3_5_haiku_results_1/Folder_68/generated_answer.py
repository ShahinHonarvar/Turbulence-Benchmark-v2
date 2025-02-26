def remove_repeat_chars(s):
    chars_count = {}
    repeat_chars = set()
    for i in range(1, 9):
        if s[i] in chars_count:
            chars_count[s[i]] += 1
            if chars_count[s[i]] > 1:
                repeat_chars.add(s[i])
        else:
            chars_count[s[i]] = 1
    result = ''.join((char for char in s if char not in repeat_chars))
    return result