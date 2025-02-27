def filter_chars(text):
    filtered_text = list(text)
    for i in range(13, 29):
        if i < len(text) and 'c' <= text[i] <= 'n':
            char = text[i]
            while char in filtered_text:
                filtered_text.remove(char)
    return ''.join(filtered_text)