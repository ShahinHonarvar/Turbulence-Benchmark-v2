def return_nth_smallest_ascii(text):
    relevant_chars = sorted(text[50:76])
    if len(relevant_chars) >= 7:
        return relevant_chars[6]
    else:
        return None