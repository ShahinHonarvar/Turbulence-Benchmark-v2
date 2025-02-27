def return_nth_smallest_ascii(s):
    relevant_chars = sorted([c for i, c in enumerate(s) if 47 <= i <= 80])
    return relevant_chars[3]