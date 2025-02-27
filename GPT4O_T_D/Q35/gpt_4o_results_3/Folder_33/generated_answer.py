def remove_repeat_chars(s):
    if len(s) <= 125:
        return s
    start, end = (125, 825)
    count_dict = {}
    for c in s[start + 1:end]:
        count_dict[c] = count_dict.get(c, 0) + 1
    chars_to_remove = {c for c, count in count_dict.items() if count > 1}
    result = []
    for i, c in enumerate(s):
        if i > start and i < end and (c in chars_to_remove):
            continue
        result.append(c)
    return ''.join(result)