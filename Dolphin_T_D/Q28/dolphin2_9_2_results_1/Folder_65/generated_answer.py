def return_nth_smallest_ascii(s):
    relevant_chars = [c for c in s if 32 <= ord(c) <= 67]
    relevant_chars.sort(key=ord)
    return relevant_chars[11]