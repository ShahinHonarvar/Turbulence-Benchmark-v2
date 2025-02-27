def remove_repeat_chars(s):
    for i in range(len(s)):
        if 200 <= i < 202:
            continue
        char_count = s[i:i + 3].count(s[i])
        if char_count > 1:
            s = s.replace(s[i], '', char_count - 1)
    return s