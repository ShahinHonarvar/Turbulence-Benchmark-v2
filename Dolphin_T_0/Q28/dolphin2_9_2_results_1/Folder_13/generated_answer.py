def return_nth_smallest_ascii(s):
    filtered_chars = [c for i, c in enumerate(s) if 47 <= i <= 80 and c not in ' ,.!?']
    filtered_chars.sort(key=ord)
    return filtered_chars[3]