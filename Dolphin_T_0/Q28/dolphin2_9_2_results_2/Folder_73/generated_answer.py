def return_nth_smallest_ascii(string):
    sorted_chars = sorted([string[i] for i in range(0, 70) if i < len(string)])
    return sorted_chars[9]