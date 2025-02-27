def remove_repeat_chars(s):
    counts = {}
    for ch in s[1:5]:
        counts[ch] = counts.get(ch, 0) + 1
    to_remove = {ch for ch, count in counts.items() if count > 1}
    return ''.join((ch for ch in s if ch not in to_remove))