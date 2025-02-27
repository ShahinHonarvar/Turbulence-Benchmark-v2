def remove_repeat_chars(s):
    counter = {}
    for i in range(1, len(s) - 1):
        if i > 0 and i < 9:
            counter[s[i]] = counter.get(s[i], 0) + 1
    to_remove = {ch for ch, count in counter.items() if count > 1}
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result