def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(100, 301):
        for j in range(i - 49, i + 1):
            if j < 0 or j > len(text) - 1:
                continue
            if text[i - j] == text[i + j]:
                palindromes.add(text[i - j:i + j + 1])
    return palindromes