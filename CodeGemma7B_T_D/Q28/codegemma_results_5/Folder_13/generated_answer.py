def return_nth_smallest_ascii(str):
    filtered_chars = [char for char in str[47:81] if char.isascii()]
    filtered_chars.sort(key=ord)
    return filtered_chars[3]