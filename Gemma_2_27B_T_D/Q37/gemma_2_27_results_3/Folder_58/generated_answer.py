def filter_chars(text):
    filtered_text = list(text)
    for i in range(503, 754):
        if i < len(filtered_text) and '9' <= filtered_text[i] <= 'w':
            char = filtered_text[i]
            filtered_text = [c for c in filtered_text if c != char]
    return ''.join(filtered_text)