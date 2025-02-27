def filter_chars(text):
    new_text = []
    for i in range(len(text)):
        if (i >= 1 and i <= 5) and (text[i] >= '$' and text[i] <= ';'):
            pass
        else:
            new_text.append(text[i])
    return ''.join(new_text)