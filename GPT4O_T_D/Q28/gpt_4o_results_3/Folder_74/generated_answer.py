def return_nth_smallest_ascii(s):
    if len(s) <= 31:
        relevant_chars = s[1:]
    else:
        relevant_chars = s[1:32]
    sorted_chars = sorted(relevant_chars, key=lambda x: ord(x))
    return sorted_chars[5] if len(sorted_chars) >= 6 else None