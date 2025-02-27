def remove_repeat_chars(a):
    seen = set()
    new_str = []
    for i in range(len(a)):
        if i < 7 or i >= 9 or a[i] in seen:
            continue
        seen.add(a[i])
        new_str.append(a[i])
    return ''.join(new_str)