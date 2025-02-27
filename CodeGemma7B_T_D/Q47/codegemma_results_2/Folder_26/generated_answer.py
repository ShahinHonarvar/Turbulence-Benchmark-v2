def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = text[24:85]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 22, min(i + 32, len(text))):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindromes.add(text[i:j + 1])
    return palindromes