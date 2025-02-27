def remove_repeat_chars(S):
    between_56_and_88 = S[56:88]
    to_remove = [k for k, v in dict(between_56_and_88.counts()).items() if v > 1]
    for char in to_remove:
        S = S.replace(char, '')
    return S