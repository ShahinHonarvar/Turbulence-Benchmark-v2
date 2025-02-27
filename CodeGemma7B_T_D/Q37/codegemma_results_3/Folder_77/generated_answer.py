def filter_chars(text):
    filtered_text = ''.join([char for char in text if (ord(char) >= ord('/') and ord(char) <= ord('8')) and (text.index(char) >= 384 and text.index(char) <= 411)])
    return filtered_text