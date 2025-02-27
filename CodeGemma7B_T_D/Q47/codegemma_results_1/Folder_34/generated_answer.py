def palindromes_of_specific_lengths(text):
    text = text.lower()
    substring = text[200:301]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 51, len(substring) + 1)):
            if substring[i:j] == substring[j - 1:i - 1:-1]:
                palindromes.add(substring[i:j])
    return palindromes