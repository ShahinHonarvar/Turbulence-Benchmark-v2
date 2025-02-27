def return_nth_smallest_ascii(s):
    filtered_chars = [ch for i, ch in enumerate(s) if 1 <= i <= 66]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[7]