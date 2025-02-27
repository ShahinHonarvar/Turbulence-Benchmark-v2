def return_nth_smallest_ascii(text):
    relevant_chars = sorted(set([text[i] for i in range(33, 86) if i < len(text)]))
    if len(relevant_chars) >= 13:
        return relevant_chars[12]
    else:
        return None