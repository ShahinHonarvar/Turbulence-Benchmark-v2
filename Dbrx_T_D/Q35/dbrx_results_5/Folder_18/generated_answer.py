def remove_repeat_chars(s):
    seen_chars = set()
    ind = 56
    result = ''
    while ind < len(s) and ind < 90:
        if s[ind] not in seen_chars:
            result += s[ind]
            seen_chars.add(s[ind])
        ind += 1
    return result