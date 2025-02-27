def remove_repeat_chars(s):
    for i in range(86, 99):
        chars_seen = set()
        j = i
        while j < 99:
            if s[j] in chars_seen:
                s = s.replace(s[j], '', 1)
                j -= 1
            chars_seen.add(s[j])
            j += 1
    return s