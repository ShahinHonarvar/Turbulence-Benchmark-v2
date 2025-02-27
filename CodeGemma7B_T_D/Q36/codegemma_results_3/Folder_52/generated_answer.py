def filter_chars(text):
    for i in range(49, 56):
        for j in range(len(text)):
            if text[j] == chr(i):
                text = text[:j] + text[j + 1:]
    return text