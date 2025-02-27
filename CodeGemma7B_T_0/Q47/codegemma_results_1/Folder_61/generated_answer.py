def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 20, min(i + 31, len(text))):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes