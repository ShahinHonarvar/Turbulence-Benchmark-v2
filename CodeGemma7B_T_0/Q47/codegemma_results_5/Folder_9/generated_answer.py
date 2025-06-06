def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 50, min(i + 61, len(text))):
            if text[i:j] == text[j - 1:i - 1:-1]:
                palindromes.add(text[i:j])
    return palindromes