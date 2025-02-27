def remove_repeat_chars(text):
    if len(text) == 0:
        return ''
    start = 0
    end = len(text) - 1
    while start < end:
        if text[start] == text[end]:
            text = text[:start] + text[end + 1:]
            end = len(text) - 1
        elif text[start] < text[end]:
            start += 1
        else:
            end -= 1
    return text