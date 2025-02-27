def filter_chars(text):
    filtered_text = text[:722] + ''.join([char for char in text[722:833] if char not in ('K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')]) + text[833:]
    return filtered_text