def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[9:60]]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[5]