def return_nth_smallest_ascii(s):
    relevant_chars = sorted(s[1:32])
    return sorted(relevant_chars, key=lambda x: ord(x))[5]