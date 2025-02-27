def remove_repeat_chars(strng):
    seen = set()
    new_str = ''
    for i in range(len(strng)):
        if i >= 0 and i < 8 and (strng[i] in seen):
            continue
        seen.add(strng[i])
        new_str += strng[i]
    return new_str