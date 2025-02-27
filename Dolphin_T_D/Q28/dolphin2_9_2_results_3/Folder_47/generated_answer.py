def return_nth_smallest_ascii(s):
    chars = []
    for i in range(3, 53):
        chars.append(s[i])
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[7]