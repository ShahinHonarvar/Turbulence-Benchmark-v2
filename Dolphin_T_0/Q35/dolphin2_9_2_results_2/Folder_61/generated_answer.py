def remove_repeat_chars(s):
    counts = [0] * 128
    for i in range(9):
        if s[i] != ' ':
            counts[ord(s[i])] += 1
    to_remove = [chr(i) for i in range(128) if counts[i] > 1]
    return ''.join([c for c in s if c not in to_remove])