def return_nth_smallest_ascii(s):
    relevant_chars = [c for c in s[11:88] if c != ' ']
    relevant_chars.sort(key=ord)
    return relevant_chars[16] if len(relevant_chars) > 16 else None