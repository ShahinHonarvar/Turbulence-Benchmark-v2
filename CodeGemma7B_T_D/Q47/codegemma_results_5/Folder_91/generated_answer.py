def palindromes_of_specific_lengths(text):
    bingo = set()
    text = text.lower()
    for i in range(len(text)):
        for k in range(i + 3, min(i + 6, len(text))):
            if text[i:k] == text[i:k][::-1]:
                bingo.add(text[i:k])
    return bingo