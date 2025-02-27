def palindromes_of_specific_lengths(text):
    text_lower = text.lower()
    palindromes = set()
    for i in range(30, 96):
        for j in range(i + 34, i + 65):
            if text_lower[i:j] == text_lower[j - 1:i - 1:-1]:
                palindromes.add(text_lower[i:j])
    return palindromes