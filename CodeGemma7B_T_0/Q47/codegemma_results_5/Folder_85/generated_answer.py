def palindromes_of_specific_lengths(text):
    text = text.lower()
    text = text[29:99]
    palindromes = set()
    for i in range(len(text) - 5):
        for j in range(i + 6, len(text) + 1):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes