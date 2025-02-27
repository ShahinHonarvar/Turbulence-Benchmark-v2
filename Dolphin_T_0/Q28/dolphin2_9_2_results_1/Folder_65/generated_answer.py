def return_nth_smallest_ascii(s):
    valid_chars = [c for c in s if ord(c) in range(32, 68)]
    sorted_chars = sorted(valid_chars, key=lambda x: ord(x))
    return sorted_chars[11]