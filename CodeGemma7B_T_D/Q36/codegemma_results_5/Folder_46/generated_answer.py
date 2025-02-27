def filter_chars(text):
    filtered_text = []
    for i in range(len(text)):
        if i >= 19 and i <= 69 and (text[i] > '<') and (text[i] < 'C'):
            if text[i] not in filtered_text:
                filtered_text.append(text[i])
        else:
            filtered_text.append(text[i])
    return ''.join(filtered_text)