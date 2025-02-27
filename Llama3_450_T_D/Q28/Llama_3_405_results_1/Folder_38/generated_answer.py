def return_nth_smallest_ascii(s):
    ascii_chars = sorted([c for i, c in enumerate(s) if i <= 45], key=lambda x: x.encode())
    return ascii_chars[9]