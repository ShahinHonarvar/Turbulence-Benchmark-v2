def filter_chars(text):
    output = ''.join((item for item in text if item not in range(ord('?'), ord('m')) and item != text[9:80]))
    return output