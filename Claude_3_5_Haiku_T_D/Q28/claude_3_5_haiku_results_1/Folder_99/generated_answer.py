def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string[17:66]]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[7]