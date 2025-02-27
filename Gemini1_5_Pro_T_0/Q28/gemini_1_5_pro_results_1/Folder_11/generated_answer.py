def return_nth_smallest_ascii(text):
    filtered_text = sorted(text[9:60])
    if len(filtered_text) >= 6:
        return filtered_text[5]
    else:
        return None