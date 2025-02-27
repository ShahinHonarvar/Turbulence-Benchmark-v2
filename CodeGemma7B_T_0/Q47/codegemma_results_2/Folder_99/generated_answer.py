def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(127, 289):
        for j in range(i - 118, i + 1):
            if j >= 0 and j < len(text) and (text[i] == text[j]):
                palindromes.add(text[j:i + 1])
    return palindromes