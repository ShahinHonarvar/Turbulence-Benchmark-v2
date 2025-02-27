def remove_repeat_chars(s):
    sub_str = s[463:995]
    char_counts = {}
    for ch in sub_str:
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1
    to_remove = {ch for ch, count in char_counts.items() if count > 1}
    result = []
    for ch in s:
        if ch not in to_remove or s.index(ch) <= 462 or s.index(ch) >= 995:
            result.append(ch)
    return ''.join(result)