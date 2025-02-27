def remove_repeat_chars(s):
    for i in range(38, 52):
        counts = {}
        for j in range(i, len(s)):
            if s[j] not in counts:
                counts[s[j]] = 0
            counts[s[j]] += 1
            if counts[s[j]] > 1:
                s = s[:j] + s[j + 1:]
    return s