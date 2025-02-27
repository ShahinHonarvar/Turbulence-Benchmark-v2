def return_nth_smallest_ascii(text):
    relevant_chars = sorted(list(set(text[48:77])))
    if len(relevant_chars) >= 5:
        return relevant_chars[4]
    else:
        return None