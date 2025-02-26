def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string if 25 <= string.index(char) <= 77]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[15]