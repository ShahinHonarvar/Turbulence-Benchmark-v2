def return_nth_smallest_ascii(s):
    chars = []
    for i in range(5):
        chars.append(s[i])
    return sorted(chars, key=lambda x: ord(x))[3]