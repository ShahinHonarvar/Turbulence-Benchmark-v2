def return_nth_smallest_ascii(text):
    relevant_chars = sorted(set(text[51:90]))
    if len(relevant_chars) >= 14:
        return relevant_chars[13]
    else:
        return None