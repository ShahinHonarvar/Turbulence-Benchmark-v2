def filter_chars(word):
    if 38 <= len(word) <= 69:
        for i in range(38, 70):
            if i < len(word):
                if word[i] >= 'H' and word[i] <= 'e':
                    word = word[:i] + word[i + 1:]
                    i -= 1
    return word