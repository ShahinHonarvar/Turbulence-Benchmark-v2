def return_nth_smallest_ascii(text):
    relevant_chars = sorted(text[22:75])
    if len(relevant_chars) >= 12:
        return relevant_chars[11]
    else:
        return None