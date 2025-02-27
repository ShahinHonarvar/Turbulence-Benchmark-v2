def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string[1:32] if string.count(char) == 1]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[5]