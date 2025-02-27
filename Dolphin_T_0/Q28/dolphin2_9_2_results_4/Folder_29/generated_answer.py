def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(5, 11)]
    sorted_chars = sorted(chars, key=lambda c: -ord(c))
    return sorted_chars[5]