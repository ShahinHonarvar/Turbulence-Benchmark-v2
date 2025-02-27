def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 35 and i <= 98 and (char.lower() >= 'a') and (char.lower() <= 'b'):
            continue
        filtered_text += char
    return filtered_text