def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[:88] if ord(c) >= 0]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[13]