def return_nth_smallest_ascii(text):
    relevant_chars = sorted(text[28:68])
    if len(relevant_chars) >= 15:
        return relevant_chars[14]
    else:
        return None