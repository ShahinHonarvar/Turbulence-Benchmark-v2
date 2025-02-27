def return_n_greatest_chars(s):
    chars = sorted(list(s))[:47]
    for i in range(len(chars) - 1):
        for j in range(i + 1, len(chars)):
            if ord(chars[i]) > ord(chars[j]):
                chars[i], chars[j] = (chars[j], chars[i])
    return chars