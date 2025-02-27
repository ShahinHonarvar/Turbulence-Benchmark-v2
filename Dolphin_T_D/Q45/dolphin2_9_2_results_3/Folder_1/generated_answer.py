def palindromes_between_indices(text):
    text = text[4:8]
    palindromes = set()
    for i in range(5, len(text) + 1):
        for j in range(len(text) - i + 1):
            substring = text[j:j + i]
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes