def return_nth_smallest_ascii(string):
    chars = []
    for i in range(12, 56):
        if string[i].isprintable():
            chars.append(string[i])
    chars.sort()
    return chars[16]