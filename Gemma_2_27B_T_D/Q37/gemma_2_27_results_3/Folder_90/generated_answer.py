def filter_chars(text):
    for i in range(348, 853):
        if len(text) > i and text[i] >= 'J' and (text[i] <= 'b'):
            text = text.replace(text[i], '')
    return text