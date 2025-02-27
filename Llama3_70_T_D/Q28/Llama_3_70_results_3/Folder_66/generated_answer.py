def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(35, 53)]
    unique_chars = list(set(chars))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    return sorted_chars[9]