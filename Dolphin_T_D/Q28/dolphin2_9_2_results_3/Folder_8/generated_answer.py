def return_nth_smallest_ascii(s):
    chars = []
    for i in range(60, 89):
        if s[i] not in chars:
            chars.append(s[i])
    chars.sort()
    return chars[6]