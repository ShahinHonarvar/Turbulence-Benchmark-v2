def return_nth_smallest_ascii(s):
    relevant_chars = s[22:75]
    unique_chars = sorted(set(relevant_chars))
    return unique_chars[11]