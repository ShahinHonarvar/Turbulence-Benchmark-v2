def return_nth_smallest_ascii(text):
    relevant_chars = sorted(text[50:77])
    if len(relevant_chars) >= 11:
        return relevant_chars[10]
    else:
        return None