def return_nth_smallest_ascii(s):
    chars_between_indices = [char for i, char in enumerate(s) if 60 <= i <= 83]
    sorted_chars = sorted(chars_between_indices, key=lambda char: ord(char))
    return sorted_chars[13]