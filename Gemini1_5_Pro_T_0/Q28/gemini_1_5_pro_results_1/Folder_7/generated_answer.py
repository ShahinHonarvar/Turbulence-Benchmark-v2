def return_nth_smallest_ascii(text):
    relevant_chars = sorted(text[12:56])
    if len(relevant_chars) >= 17:
        return relevant_chars[16]
    else:
        return None