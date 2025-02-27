def return_nth_smallest_ascii(text):
    filtered_text = ''.join(sorted([text[i] for i in range(51, 90) if i < len(text)]))
    if len(filtered_text) >= 14:
        return filtered_text[13]
    else:
        return None