def remove_repeat_chars(text):
    left_boundary = 50
    right_boundary = 200
    unique_chars = []
    for i in range(left_boundary, right_boundary):
        if text[i] not in unique_chars:
            unique_chars.append(text[i])
    modified_text = []
    for i in range(len(text)):
        if text[i] in unique_chars:
            modified_text.append(text[i])
    return ''.join(modified_text)