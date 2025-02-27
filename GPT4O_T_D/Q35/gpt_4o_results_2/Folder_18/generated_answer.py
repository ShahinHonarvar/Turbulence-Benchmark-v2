def remove_repeat_chars(s):
    count = {}
    for ch in s[57:90]:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    remove_chars = {ch for ch, c in count.items() if c > 1}
    return ''.join((ch for ch in s if ch not in remove_chars))