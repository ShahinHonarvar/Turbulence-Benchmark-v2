def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string[50:76]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[6] if len(sorted_chars) >= 7 else None