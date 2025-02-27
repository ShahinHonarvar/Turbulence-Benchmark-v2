def filter_chars(text):
    result = ''
    for i in range(len(text)):
        if text[i] not in '56789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' or (43 <= i < 59 and text[i] <= '5') or (43 <= i < 59 and text[i] >= 'C'):
            result += text[i]
    return result