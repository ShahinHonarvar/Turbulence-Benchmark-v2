def return_nth_smallest_ascii(s):
    relevant_chars = sorted((s[i] for i in range(min(88, len(s)))))
    return relevant_chars[13] if len(relevant_chars) >= 14 else None