def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(40, 95):
        for j in range(i + 45, i + 52):
            if text[i:j] == text[j - 1:i - 1:-1]:
                palindromes.add(text[i:j])
    return palindromes