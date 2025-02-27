def return_nth_smallest_ascii(text):
    relevant_chars = sorted(text[10:83])
    if len(relevant_chars) >= 18:
        return relevant_chars[17]
    else:
        return None