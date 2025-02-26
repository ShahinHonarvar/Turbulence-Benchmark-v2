def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s if 8 <= s.index(char) <= 65]
    return sorted(filtered_chars)[5]