def remove_repeat_chars(str):
    seen = set()
    for i in range(125, 825):
        ch = str[i]
        if ch in seen:
            str = str.replace(ch, '', str.count(ch))
        else:
            seen.add(ch)
    return str