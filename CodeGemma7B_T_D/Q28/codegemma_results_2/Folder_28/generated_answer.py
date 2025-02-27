def return_nth_smallest_ascii(char_list):
    filtered_chars = char_list[25:78]
    sorted_chars = sorted(filtered_chars, key=ord)
    return sorted_chars[15]