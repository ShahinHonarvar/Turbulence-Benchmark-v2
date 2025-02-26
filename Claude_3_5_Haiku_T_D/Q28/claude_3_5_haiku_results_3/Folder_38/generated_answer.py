def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[:46]]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[9] if len(sorted_chars) >= 10 else None