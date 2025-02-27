def return_nth_smallest_ascii(s):
    chars = []
    for i in range(5):
        if s[i] not in chars:
            chars.append(s[i])
    chars.sort(key=ord)
    return chars[4]