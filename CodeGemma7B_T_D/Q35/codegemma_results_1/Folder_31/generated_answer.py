def remove_repeat_chars(text):
    processed_text = text
    for i in range(33, 78):
        char = processed_text[i]
        if processed_text.count(char) > 1:
            processed_text = processed_text.replace(char, '', processed_text.count(char) - 1)
    return processed_text