def return_nth_smallest_ascii(text):
    filtered_text = sorted(text[12:73])
    if len(filtered_text) >= 13:
        return filtered_text[12]
    else:
        return None