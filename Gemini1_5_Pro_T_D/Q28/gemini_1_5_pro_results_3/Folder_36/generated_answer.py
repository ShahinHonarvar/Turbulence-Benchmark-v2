def return_nth_smallest_ascii(text):
    relevant_chars = sorted(text[17:57])
    if len(relevant_chars) >= 9:
        return relevant_chars[8]
    else:
        return None