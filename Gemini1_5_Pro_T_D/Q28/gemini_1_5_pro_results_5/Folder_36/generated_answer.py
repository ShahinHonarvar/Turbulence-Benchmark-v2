def return_nth_smallest_ascii(text):
    filtered_text = sorted(text[17:57])
    if len(filtered_text) >= 9:
        return filtered_text[8]
    else:
        return None