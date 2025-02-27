def return_nth_smallest_ascii(s):
    relevant_chars = s[:8]
    sorted_chars = sorted(relevant_chars, key=lambda x: ord(x))
    return sorted_chars[7]