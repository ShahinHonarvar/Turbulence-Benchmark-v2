def return_nth_smallest_ascii(text):
    relevant_chars = sorted(set(text[32:68]))
    if len(relevant_chars) >= 12:
        return relevant_chars[11]
    else:
        return None