def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string if string.index(char) >= 0 and string.index(char) <= 87]
    filtered_chars.sort(key=ord)
    return filtered_chars[13]