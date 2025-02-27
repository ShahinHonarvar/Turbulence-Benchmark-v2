def remove_repeat_chars(s):
    counts = [0] * 128
    for char in s:
        if ord(char) < 128:
            counts[ord(char)] += 1
    for i in range(27, 97):
        if counts[i] > 1:
            s = ''.join((c for c in s if c != chr(i)))
    return s