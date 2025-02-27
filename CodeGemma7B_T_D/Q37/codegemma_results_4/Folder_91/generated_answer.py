def filter_chars(text):
    new_text = []
    for i in range(len(text)):
        if text[i] in 'B' <= text[i] <= 'H' and 7 <= i <= 8:
            continue
        else:
            new_text.append(text[i])
    return ''.join(new_text)