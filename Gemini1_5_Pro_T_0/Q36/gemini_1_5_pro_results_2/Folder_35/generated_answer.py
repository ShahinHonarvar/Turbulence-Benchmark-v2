def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if 163 < i < 658 and '(' < text[i] < ']':
            new_text += ''
        else:
            new_text += text[i]
    return new_text