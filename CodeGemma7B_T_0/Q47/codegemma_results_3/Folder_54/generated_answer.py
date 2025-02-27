def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = text[27:78]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 18, i + 20):
            if j <= len(text) and text[i:j] == text[j - 1:i - 1:-1]:
                palindromes.add(text[i:j])
    return palindromes