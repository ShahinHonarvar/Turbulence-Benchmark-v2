def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string if string.index(char) <= 87]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[13]