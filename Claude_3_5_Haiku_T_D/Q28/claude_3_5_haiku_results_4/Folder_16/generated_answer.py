def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[18:46]]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[6]