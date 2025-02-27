def remove_repeat_chars(s):
    chars = {}
    start, end = (30, 200)
    for i in range(len(s)):
        if i >= start and i < end:
            if s[i] in chars:
                chars[s[i]] += 1
                if chars[s[i]] > 1:
                    s = s[:i] + s[i + 1:]
            else:
                chars[s[i]] = 1
        elif i >= end:
            break
    return s