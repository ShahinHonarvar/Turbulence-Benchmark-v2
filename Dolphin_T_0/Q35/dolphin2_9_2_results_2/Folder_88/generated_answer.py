def remove_repeat_chars(s):
    chars = [c for c in s[3:9]]
    for i in range(len(chars)):
        if chars.count(chars[i]) > 1:
            s = s.replace(chars[i], '')
    return s