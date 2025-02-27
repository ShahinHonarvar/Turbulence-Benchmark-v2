def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 32 <= i <= 67]
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[11]