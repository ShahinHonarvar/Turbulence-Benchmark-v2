def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        if 35 <= i <= 51 and 'H' <= text[i] <= 's':
            for char in text:
                if char != text[i]:
                    new_text += char
            text = new_text
            new_text = ''
        else:
            new_text += text[i]
    return new_text