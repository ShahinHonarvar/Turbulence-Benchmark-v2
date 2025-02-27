def return_nth_smallest_ascii(text):
    relevant_chars = [c for i, c in enumerate(text) if 32 <= i <= 67]
    relevant_chars.sort(key=ord)
    return relevant_chars[11]