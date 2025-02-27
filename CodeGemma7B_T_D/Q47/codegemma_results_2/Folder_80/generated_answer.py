def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text[35:89].lower()
    for i in range(len(text) - 3):
        for j in range(i + 24, min(i + 34, len(text))):
            if text[i] == text[j] and text[i + 1] == text[j - 1]:
                palindromes.add(''.join(text[i:j + 1]))
    return palindromes