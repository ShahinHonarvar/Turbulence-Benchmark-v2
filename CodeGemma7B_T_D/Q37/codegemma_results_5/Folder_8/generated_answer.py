def filter_chars(text_input):
    filtered_text = ''
    for i in range(len(text_input)):
        if i >= 41 and i <= 86 and (text_input[i] >= 'S') and (text_input[i] <= 's'):
            pass
        else:
            filtered_text += text_input[i]
    return filtered_text