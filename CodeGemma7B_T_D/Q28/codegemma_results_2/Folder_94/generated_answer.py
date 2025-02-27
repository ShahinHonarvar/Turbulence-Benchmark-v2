def return_nth_smallest_ascii(text):
    sorted_chars = sorted([char for char in text if char != ' '], key=ord)
    return sorted_chars[18][0]