def return_nth_smallest_ascii(text):
    relevant_chars = sorted(text[10:91])
    if len(relevant_chars) >= 20:
        return relevant_chars[19]
    else:
        return None