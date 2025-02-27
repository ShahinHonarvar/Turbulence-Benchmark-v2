def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    text = text[44:99 + 1]
    for i in range(len(text) - 12):
        for j in range(i + 2, min(i + 43, len(text))):
            if text[i:j] == text[j - 1:i - 1:-1]:
                palindromes.add(text[i:j])
    return palindromes