def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s if 10 <= s.index(char) <= 90]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[19]