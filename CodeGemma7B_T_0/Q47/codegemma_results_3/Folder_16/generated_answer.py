def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(15, 87):
        for j in range(i + 51, i + 61):
            if text[i:j] == text[j - 1:i - 1:-1]:
                palindromes.add(text[i:j])
    return palindromes