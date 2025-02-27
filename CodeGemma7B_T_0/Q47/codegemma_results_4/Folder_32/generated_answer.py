def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(16, 78):
        for j in range(i - 47, i - 42):
            if j >= 0 and text[i] == text[j]:
                palindromes.add(text[j:i + 1])
    return palindromes