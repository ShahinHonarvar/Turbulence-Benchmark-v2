def return_nth_smallest_ascii(arg):
    filtered_chars = [char for char in arg if 3 <= arg.index(char) <= 52]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[7] if len(sorted_chars) > 7 else None