def remove_repeat_chars(text):
    freq = {}
    for c in text[17:88]:
        if not c in freq:
            freq[c] = 0
        freq[c] += 1
    result = ''
    for c in text:
        if c not in freq.keys() or freq[c] == 1:
            result += c
    return result