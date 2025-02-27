def remove_repeat_chars(s):
    start, end = (58, 85)
    sub_str = s[start + 1:end]
    char_count = {}
    for ch in sub_str:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    repeat_chars = {ch for ch, count in char_count.items() if count > 1}
    result = [ch for ch in s if ch not in repeat_chars or not start < s.index(ch) < end]
    return ''.join(result)