def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower().strip()
    for i in range(36, 93):
        for j in range(i + 10, 93):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindromes.add(text[i:j + 1])
    return palindromes