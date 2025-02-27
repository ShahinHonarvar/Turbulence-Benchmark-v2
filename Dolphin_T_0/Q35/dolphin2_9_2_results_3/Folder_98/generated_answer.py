def remove_repeat_chars(text):
    chars = {}
    for i in range(8):
        if text[i] in chars:
            chars[text[i]] += 1
        else:
            chars[text[i]] = 1
    res = [c for c in text if chars[c] < 2]
    return ''.join(res)