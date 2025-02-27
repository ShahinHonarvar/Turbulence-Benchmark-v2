def filter_chars(text: str) -> str:
    filtered_text = ''
    for c in text.replace('', ''):
        if ord(c) >= 124 and ord(c) <= 854 and (ord(c) >= ord('9')) and (ord(c) <= ord('s')):
            continue
        filtered_text += c
    return filtered_text