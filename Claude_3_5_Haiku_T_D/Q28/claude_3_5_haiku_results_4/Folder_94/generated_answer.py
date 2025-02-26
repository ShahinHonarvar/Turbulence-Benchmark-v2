def return_nth_smallest_ascii(s):
    filtered_chars = [c for c in s[6:59]]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[18]