def filter_chars(text):
    filtered_text = []
    for i, char in enumerate(text):
        if i > 586 and i < 648 and (char > ',') and (char < 'c'):
            continue
        filtered_text.append(char)
    return ''.join(filtered_text)