def remove_repeat_chars(s):
    counts = {}
    for ch in s[3:7]:
        counts[ch] = counts.get(ch, 0) + 1
    result = ''.join((ch for ch in s if counts.get(ch, 0) < 2 or s.index(ch) <= 2 or s.index(ch) >= 7))
    return result