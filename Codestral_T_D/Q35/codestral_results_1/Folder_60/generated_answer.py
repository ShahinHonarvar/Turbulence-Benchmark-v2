def remove_repeat_chars(s):
    counts = {}
    for i in range(38, 52):
        ch = s[i]
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    chars_to_remove = [ch for ch, count in counts.items() if count > 1]
    return ''.join((ch for ch in s if ch not in chars_to_remove))