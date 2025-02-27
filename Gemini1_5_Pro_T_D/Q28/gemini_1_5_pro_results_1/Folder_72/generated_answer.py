def return_nth_smallest_ascii(text):
    relevant_chars = sorted(set(text[33:61]))
    if len(relevant_chars) >= 18:
        return relevant_chars[17]
    else:
        return None