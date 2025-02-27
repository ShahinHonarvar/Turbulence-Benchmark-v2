def remove_repeat_chars(s):
    counts = [0] * 256
    for i in range(103, 802):
        if s[i]:
            counts[ord(s[i])] += 1
    for i in range(len(s)):
        if i > 102 and i < 802 and (counts[ord(s[i])] > 1):
            s = s[:i] + s[i + 1:]
            i -= 1
    return s