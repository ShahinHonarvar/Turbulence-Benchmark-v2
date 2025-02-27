def return_nth_smallest_ascii(s):
    relevant_chars = sorted([ord(s[i]) for i in range(min(46, len(s)))])
    return chr(relevant_chars[9])