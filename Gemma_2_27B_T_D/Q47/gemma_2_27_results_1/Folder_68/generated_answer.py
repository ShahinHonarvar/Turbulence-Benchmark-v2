def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(51):
        for j in range(i + 50, min(i + 101, len(text))):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes